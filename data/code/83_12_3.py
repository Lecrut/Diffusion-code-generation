from datetime import datetime
class DateComparator:
    def check_equality(self, date_str1, date_str2):
        try:
            date1 = datetime.strptime(date_str1, '%Y-%m-%d')
            date2 = datetime.strptime(date_str2, '%Y-%m-%d')
            return date1 == date2
        except ValueError:
            return False
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-27"
    date_b = "2023-10-27"
    date_c = "2023-10-28"
    date_d = "2023/10/27"
    date_e = "2023-10-27T10:00:00"
    print(f"Comparing {date_a} and {date_b}: {comparator.check_equality(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {comparator.check_equality(date_a, date_c)}")
    print(f"Comparing {date_a} and {date_d}: {comparator.check_equality(date_a, date_d)}")
    print(f"Comparing {date_a} and {date_e}: {comparator.check_equality(date_a, date_e)}")