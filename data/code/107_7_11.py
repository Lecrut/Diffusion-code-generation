from datetime import datetime

class TimestampConverter:
    @staticmethod
    def timestamp_to_iso(unix_timestamp):
        dt_object = datetime.utcfromtimestamp(unix_timestamp)
        return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    converter = TimestampConverter()
    iso1 = converter.timestamp_to_iso(1633072800)
    print(iso1)
    iso2 = converter.timestamp_to_iso(946684800)
    print(iso2)