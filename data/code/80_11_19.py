from datetime import datetime

class DateComparator:
    def compare(self, date1_str, date2_str):
        date1 = datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.strptime(date2_str, '%Y-%m-%d').date()
        if date1 < date2:
            return (date1, date2)
        else:
            return (date2, date1)

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.compare("2023-10-26", "2023-10-25")
    print(f"Comparing 2023-10-26 and 2023-10-25: {result1}")
    result2 = comparator.compare("2024-01-01", "2023-12-31")
    print(f"Comparing 2024-01-01 and 2023-12-31: {result2}")
    result3 = comparator.compare("1999-01-01", "2025-05-10")
    print(f"Comparing 1999-01-01 and 2025-05-10: {result3}")