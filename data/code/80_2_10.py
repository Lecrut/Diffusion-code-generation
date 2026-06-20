import datetime

class DateComparator:
    def compare(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        return (date1_str, date2_str) if date1 < date2 else (date2_str, date1_str)

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.compare("2023-01-15", "2023-01-01")
    print(f"Comparing 2023-01-15 and 2023-01-01: {result1}")
    result2 = comparator.compare("2024-05-20", "2023-01-15")
    print(f"Comparing 2024-05-20 and 2023-01-15: {result2}")