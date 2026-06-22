from datetime import datetime

class DateProcessor:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, DateProcessor.DATE_FORMAT)

    @staticmethod
    def get_day_of_month(date_string):
        dt = DateProcessor.parse_date(date_string)
        return dt.day

if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-02-29", "2025-12-31"]
    processor = DateProcessor()
    results = [processor.get_day_of_month(d) for d in sample_dates]
    print(results)