from datetime import datetime

class DateFormatter:
    INPUT_FORMAT = "%Y-%m-%d"
    OUTPUT_FORMAT = "%d/%m/%Y"

    @staticmethod
    def parse(date_string: str) -> datetime:
        return datetime.strptime(date_string, DateFormatter.INPUT_FORMAT)

    @staticmethod
    def format(date_string: str) -> str:
        parsed = DateFormatter.parse(date_string)
        return parsed.strftime(DateFormatter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = "2024-01-15"
    formatted_date = DateFormatter.format(sample_date)
    print(formatted_date)