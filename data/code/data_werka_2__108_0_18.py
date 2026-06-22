import datetime

class DateParser:
    DAY_COMPONENT = "day"

    @staticmethod
    def get_day_of_month(date_obj: datetime.date) -> int:
        if not isinstance(date_obj, datetime.date):
            raise ValueError("Input must be a datetime.date object")
        return date_obj.day

if __name__ == '__main__':
    sample_date = datetime.date(2024, 1, 31)
    parser = DateParser()
    result = parser.get_day_of_month(sample_date)
    print(result)