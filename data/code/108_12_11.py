from datetime import datetime

class DateExtractor:
    def extract_day(self, date_string: str) -> int:
        try:
            date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
            return date_object.day
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DDTHH:MM:SS.")

if __name__ == '__main__':
    extractor = DateExtractor()
    timestamp1 = "2024-07-04T12:00:00"
    print(f"Day extracted from {timestamp1}: {extractor.extract_day(timestamp1)}")