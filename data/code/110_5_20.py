from datetime import datetime

class ChronologicalSorter:
    def __init__(self, dates):
        self.dates = dates

    def sort(self):
        return sorted(self.dates, key=lambda d: datetime.strptime(d, '%d/%m/%Y'))

if __name__ == '__main__':
    dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorter = ChronologicalSorter(dates)
    print(sorter.sort())
    print(len(dates))