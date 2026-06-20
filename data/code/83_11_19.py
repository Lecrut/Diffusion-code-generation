import datetime

class DateComparator:
    def check_equality(self, date_str1, date_str2):
        return datetime.datetime.strptime(date_str1, '%Y-%m-%d').date() == datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = '2023-10-26'
    date_b = '2023-10-26'
    date_c = '2023-10-27'
    date_d = '2024-10-26'

    print(f"Are {date_a} and {date_b} identical? {comparator.check_equality(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {comparator.check_equality(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {comparator.check_equality(date_a, date_d)}")
    print(f"Are {date_b} and {date_d} identical? {comparator.check_equality(date_b, date_d)}")