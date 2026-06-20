import datetime

class DateComparator:
    def check_equality(self, date1_str, date2_str):
        try:
            date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
            date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
            return date1.date() == date2.date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-26"
    date_b = "2023-10-26"
    date_c = "2023-10-27"
    date_d = "2024-10-26"
    
    print(f"Are {date_a} and {date_b} identical? {comparator.check_equality(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {comparator.check_equality(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {comparator.check_equality(date_a, date_d)}")