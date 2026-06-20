from datetime import datetime

class DateComparator:
    def check_equality(self, date_str1, date_str2):
        try:
            return datetime.strptime(date_str1, '%Y-%m-%d') == datetime.strptime(date_str2, '%Y-%m-%d')
        except ValueError:
            return False

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-27"
    date_b = "2023-10-27"
    date_c = "2023-10-28"
    print(f"Comparing {date_a} and {date_b}: {comparator.check_equality(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {comparator.check_equality(date_a, date_c)}")