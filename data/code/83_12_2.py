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
    date1 = "2023-10-27"
    date2 = "2023-10-27"
    date3 = "2023-10-28"
    date4 = "2023-10-27"
    date5 = "2023-10-27T10:00:00"
    print(f"Comparing {date1} and {date2}: {comparator.check_equality(date1, date2)}")
    print(f"Comparing {date1} and {date3}: {comparator.check_equality(date1, date3)}")
    print(f"Comparing {date1} and {date4}: {comparator.check_equality(date1, date4)}")
    print(f"Comparing {date1} and {date5}: {comparator.check_equality(date1, date5)}")