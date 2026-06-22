from datetime import datetime

class ISO8601Converter:
    def convert(self):
        now = datetime.now()
        return now.isoformat(timespec='microseconds')

if __name__ == '__main__':
    converter = ISO8601Converter()
    print(converter.convert())