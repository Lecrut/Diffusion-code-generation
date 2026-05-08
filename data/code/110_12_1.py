from datetime import datetime
class DateSorter:
    def sort_dates(self, date_strings):
        date_objects = []
        for date_str in date_strings:
            try:
                date_objects.append(datetime.strptime(date_str, '%Y-%m-%d'))
            except ValueError:
                pass
        date_objects.sort()
        sorted_date_strings = [d.strftime('%Y-%m-%d') for d in date_objects]
        return sorted_date_strings
if __name__ == '__main__':
    sorter = DateSorter()
    unsorted_dates = [
        "2023-10-26",
        "2023-01-15",
        "2024-05-01",
        "2023-12-31",
        "2023-03-10"
    ]
    sorted_dates = sorter.sort_dates(unsorted_dates)
    print(sorted_dates)