from datetime import datetime

class DateSorter:
    def __init__(self, dates):
        self.original_dates = list(dates)
        self.sorted_dates = self._process()

    def _process(self):
        results = []
        for d in self.original_dates:
            results.append(self._validate_and_convert(d))
        results.sort(key=lambda x: x[0])
        return [x[1] for x in results]

    def _validate_and_convert(self, date_str):
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError(f"Bad format: {date_str}")
        try:
            m = int(parts[0])
            d = int(parts[1])
            y = int(parts[2])
        except ValueError:
            raise ValueError(f"Not integers: {date_str}")
        
        if not (1 <= m <= 12):
            raise ValueError(f"Month out of range: {m}")
        if not (1 <= d <= 31):
            raise ValueError(f"Day out of range: {d}")
        if len(parts[2]) != 4:
            raise ValueError(f"Year must be 4 digits: {parts[2]}")

        return (datetime(y, m, d), date_str)

    def get_sorted(self):
        return self.sorted_dates

    def get_original(self):
        return self.original_dates

if __name__ == '__main__':
    data = ['12-31-2023', '01-01-2023', '06-15-2022', '02-28-2023']
    sorter = DateSorter(data)
    print(sorter.get_sorted())
    print(sorter.get_original())