from datetime import datetime

class DateFormatter:
    DATE_FORMAT = "%d %B %Y"

    @staticmethod
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime(DateFormatter.DATE_FORMAT)

if __name__ == '__main__':
    sample_date = "2022-11-11"
    result = DateFormatter.format_date(sample_date)
    print(result)