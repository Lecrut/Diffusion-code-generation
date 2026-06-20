import datetime

class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = datetime.date(2023, 10, 5)
    date_b = datetime.date(2023, 10, 5)
    date_c = datetime.date(2023, 10, 6)
    
    result_ab = comparator.check_equality(date_a, date_b)
    result_ac = comparator.check_equality(date_a, date_c)
    
    print(f"Comparing {date_a} and {date_b}: {result_ab}")
    print(f"Comparing {date_a} and {date_c}: {result_ac}")