import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"
    
    @staticmethod
    def compare(date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, DateComparator.DATE_FORMAT)
        date2 = datetime.datetime.strptime(date2_str, DateComparator.DATE_FORMAT)
        if date1 < date2:
            return (date1_str, date2_str)
        elif date1 > date2:
            return (date2_str, date1_str)
        else:
            return (date1_str, date2_str)

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-01"
    result1 = comparator.compare(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    date_c = "2024-05-20"