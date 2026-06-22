from datetime import datetime

class DateSorter:
    def __init__(self, dates):
        self.dates = list(dates)

    def get_sorted(self):
        parsed = []
        for d in self.dates:
            parts = d.split('/')
            if len(parts) != 3:
                raise ValueError(f"Invalid date: {d}")
            try:
                day = int(parts[0])
                month = int(parts[1])
                year = int(parts[2])
            except ValueError:
                raise ValueError(f"Invalid date: {d}")
            dt = datetime(year=year, month=month, day=day)
            parsed.append((dt, d))
        parsed.sort(key=lambda x: x[0])
        return [item[1] for item in parsed]

if __name__ == '__main__':
    sample_dates = ['10/02/2021', '05/01/2021', '25/12/2020', '01/01/2021']
    sorter = DateSorter(sample_dates)
    result = sorter.get_sorted()
    print(result)
    sample_dates_2 = ['31/12/2023', '01/01/2024', '15/06/2023']
    sorter_2 = DateSorter(sample_dates_2)
    result_2 = sorter_2.get_sorted()
    print(result_2)