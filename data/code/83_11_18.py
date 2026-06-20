import datetime

class DateComparator:
    @staticmethod
    def validate_date(date_str):
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def check_equality(date1, date2):
        if not (DateComparator.validate_date(date1) and DateComparator.validate_date(date2)):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        return datetime.datetime.strptime(date1, '%Y-%m-%d') == datetime.datetime.strptime(date2, '%Y-%m-%d')

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = '2023-10-26'
    date_b = '2023-10-26'
    date_c = '2023-10-27'
    date_d = '2024-10-26'

    print(f"Are {date_a} and {date_b} identical? {comparator.check_equality(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {comparator.check_equality(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {comparator.check_equality(date_a, date_d)}")