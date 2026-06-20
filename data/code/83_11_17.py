import datetime

class DateComparator:
    def check_equality(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
        return date1.date() == date2.date()

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-26"
    date_b = "2023-10-26"
    date_c = "2023-10-27"
    date_d = "2024-10-26"
    
    print(f"Are {date_a} and {date_b} identical? {comparator.check_equality(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {comparator.check_equality(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {comparator.check_equality(date_a, date_d)}")
    print(f"Are {date_b} and {date_d} identical? {comparator.check_equality(date_b, date_d)}")