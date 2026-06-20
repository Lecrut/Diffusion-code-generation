import datetime

class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = datetime.date(2023, 9, 15)
    date_b = datetime.date(2023, 9, 15)
    date_c = datetime.date(2023, 9, 16)
    
    print(f"Comparing {date_a} and {date_b}: {comparator.check_equality(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {comparator.check_equality(date_a, date_c)}")