import datetime

class DateComparator:
    def compare(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        return (date1_str, date2_str) if date1 < date2 else (date2_str, date1_str)

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-04-15"
    date_b = "2023-03-20"
    result1 = comparator.compare(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    date_c = "2024-06-01"