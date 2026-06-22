from datetime import date

class DateSorter:
    def __init__(self, raw_dates):
        self._validate(raw_dates)
        self.dates = [date(*d) for d in raw_dates]

    def _validate(self, raw_dates):
        if not isinstance(raw_dates, list):
            raise ValueError("Input must be a list")
        for item in raw_dates:
            if not isinstance(item, (list, tuple)) or len(item) != 3:
                raise ValueError("Each item must be a tuple or list of 3 integers")
            year, month, day = item
            if not all(isinstance(x, int) for x in (year, month, day)):
                raise ValueError("Year, month, and day must be integers")

    def get_sorted_oldest_to_newest(self):
        return sorted(self.dates)

if __name__ == '__main__':
    raw_data = [(2023, 10, 5), (2019, 2, 14), (2021, 8, 30)]
    sorter = DateSorter(raw_data)
    print(sorter.get_sorted_oldest_to_newest())