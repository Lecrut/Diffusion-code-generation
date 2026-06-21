from datetime import datetime

class DateConverter:
    SOURCE_FORMAT = "%d-%m-%Y %H:%M:%S"
    TARGET_FORMAT = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def convert(date_string: str) -> str:
        parsed = datetime.strptime(date_string, DateConverter.SOURCE_FORMAT)
        return parsed.strftime(DateConverter.TARGET_FORMAT)

if __name__ == '__main__':
    sample_date = '15-08-2024 09:15:30'
    converted_date = DateConverter.convert(sample_date)
    print(converted_date)