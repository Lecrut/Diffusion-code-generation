import datetime

class DateSorter:
    @staticmethod
    def sort_datetime_list(datetime_list):
        return sorted(datetime_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime.datetime(2023, 4, 1),
        datetime.datetime(2022, 1, 15),
        datetime.datetime(2023, 3, 20)
    ]
    sorter = DateSorter()
    sorted_datetimes = sorter.sort_datetime_list(sample_datetimes)
    print(sorted_datetimes)