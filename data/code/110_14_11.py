import datetime

class DateSorter:
    def __init__(self, date_strings):
        self.date_objects = []
        for date_str in date_strings:
            try:
                self.date_objects.append(datetime.datetime.strptime(date_str, "%Y-%m-%d"))
            except ValueError:
                print(f"Error parsing date: {date_str}")

    def sort_dates(self):
        self.date_objects.sort(reverse=True)

    def get_sorted_dates(self):
        return [dt.strftime("%Y-%m-%d") for dt in self.date_objects]

if __name__ == '__main__':
    sorter = DateSorter([
        "2023-10-26",
        "2022-11-15",
        "2024-01-01",
        "2023-05-10"
    ])
    sorter.sort_dates()
    print("Sorted Dates:")
    for date in sorter.get_sorted_dates():
        print(date)