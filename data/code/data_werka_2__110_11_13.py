from datetime import datetime

class DateTimeSorter:
    def __init__(self, datetimes):
        self.datetimes = list(datetimes)

    def sort(self):
        return sorted(self.datetimes)

    def get_earliest(self):
        if not self.datetimes:
            return None
        return min(self.datetimes)

    def get_latest(self):
        if not self.datetimes:
            return None
        return max(self.datetimes)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2023, 10, 1, 12, 0),
        datetime(2021, 5, 15, 8, 30),
        datetime(2022, 1, 1, 0, 0),
        datetime(2023, 1, 1, 23, 59),
        datetime(2020, 12, 31, 18, 45),
    ]
    sorter = DateTimeSorter(sample_datetimes)
    sorted_result = sorter.sort()
    print(sorted_result)
    print(sorter.get_earliest())
    print(sorter.get_latest())