import datetime

class DateSorter:
    DATE_FORMAT = "%Y-%m-%d"
    
    @staticmethod
    def parse_date(date_str):
        try:
            return datetime.datetime.strptime(date_str, DateSorter.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Error parsing date: {date_str}")
    
    @classmethod
    def sort_dates(cls, date_strings):
        date_objects = [cls.parse_date(date_str) for date_str in date_strings]
        date_objects.sort(reverse=True)
        return date_objects

if __name__ == '__main__':
    date_strings = [
        "2023-10-26",
        "2022-11-15",
        "2024-01-01",
        "2023-05-10"
    ]
    
    sorted_dates = DateSorter.sort_dates(date_strings)
    print("Sorted Dates:")
    for dt in sorted_dates:
        print(dt.strftime(DateSorter.DATE_FORMAT))