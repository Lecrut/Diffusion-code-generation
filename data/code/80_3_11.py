from datetime import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def is_strictly_before(date1, date2):
        return date1 < date2

if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-20"
    
    try:
        date1 = datetime.strptime(date_str1, DateComparator.DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DateComparator.DATE_FORMAT)
    except ValueError:
        print("Error: Invalid date format provided.")
    else:
        result = DateComparator.is_strictly_before(date1, date2)
        print(f"Is date1 strictly before date2? {result}")