from datetime import datetime

class TimestampParser:
    def parse_day(self, timestamp: str) -> int:
        try:
            date_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
            return date_object.day
        except ValueError:
            raise ValueError("Invalid timestamp format. Please use YYYY-MM-DDTHH:MM:SS.")

if __name__ == '__main__':
    parser = TimestampParser()
    timestamp1 = "2024-07-04T12:00:00"
    timestamp2 = "2023-11-15T08:30:00"
    print(f"Day for {timestamp1}: {parser.parse_day(timestamp1)}")
    print(f"Day for {timestamp2}: {parser.parse_day(timestamp2)}")