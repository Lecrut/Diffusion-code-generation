from datetime import datetime

class DateTimeSorter:
    def sort_datetime_list(self, dt_list):
        return sorted(dt_list)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 1, 5),
        datetime(2022, 12, 25),
        datetime(2023, 1, 1)
    ]
    sorter = DateTimeSorter()
    sorted_dates = sorter.sort_datetime_list(sample_dates)
    print(sorted_dates)