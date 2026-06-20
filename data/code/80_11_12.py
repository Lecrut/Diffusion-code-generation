import datetime

class DateComparator:
    @staticmethod
    def validate_date_format(date_str):
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @classmethod
    def compare(cls, date1_str, date2_str):
        if not (cls.validate_date_format(date1_str) and cls.validate_date_format(date2_str)):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()

        if date1 < date2:
            return (date1, date2)
        else:
            return (date2, date1)

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.compare("2023-10-26", "2023-10-25")
    print(f"Comparing 2023-10-26 and 2023-10-25: {result1}")
    result2 = comparator.compare("2024-01-01", "2023-12-31")
    print(f"Comparing 2024-01-01 and 2023-12-31: {result2}")
    try:
        result3 = comparator.compare("invalid-date", "2023-10-25")
        print(f"Comparing invalid-date and 2023-10-25: {result3}")
    except ValueError as e:
        print(e)