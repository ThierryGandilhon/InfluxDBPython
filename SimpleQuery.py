import argparse

from influxdb import InfluxDBClient


def main(host='localhost', port=8086, user='root', password='root', database='example', query='select * from mesure'):
    client = InfluxDBClient(host, port, user, password, database)

    print("Queying data: " + query)
    result = client.query(query)

    print("Result: {0}".format(result))



def parse_args():
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False, default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    parser.add_argument('--user', type=str, required=False, default='root',
                        help='user name to connect to InfluxDB http API')
    parser.add_argument('--password', type=str, required=False, default='root',
                        help='password to connect to InfluxDB http API')
    parser.add_argument('--database', type=str, required=False, default='example',
                        help='database to connect to InfluxDB http API')
    parser.add_argument('--query', type=str, required=True, default='select * fro mesure',
                        help='query to execute on InfluxDB')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port, user=args.user, password=args.password, database=args.database, query=args.query)
