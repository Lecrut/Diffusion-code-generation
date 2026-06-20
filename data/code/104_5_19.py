from datetime import datetime

class DateTimeComparator:
    @staticmethod
    def compare_dates(date1_str, date2_str):
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        if date1 < date2:
            return 'First is earlier'
        elif date2 < date1:
            return 'Second is earlier'
        else:
            return 'They are equal'

if __name__ == '__main__':
    comparator = DateTimeComparator()
    print(comparator.compare_dates("2023-01-15", "2023-02-01"))
    print(comparator.compare_dates("2023-02-01", "2023-01-15"))
    print(comparator.compare_dates("2023-10-20", "2023-10-20"))