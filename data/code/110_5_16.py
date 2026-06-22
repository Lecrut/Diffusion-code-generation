from datetime import datetime

class DateSorter:
    def __init__(self):
        self.format_str = '%d/%m/%Y'

    def parse(self, date_str):
        if not isinstance(date_str, str):
            raise ValueError("Date must be a string")
        return datetime.strptime(date_str, self.format_str)

    def sort(self, dates):
        if not dates:
            return []
        validated = [self.parse(d) for d in dates]
        paired = list(zip(validated, dates))
        paired.sort(key=lambda x: x[0])
        return [d[1] for d in paired]

if __name__ == '__main__':
    sorter = DateSorter()
    raw_dates = ['12/01/2020', '31/12/2019', '01/01/2021']
    result = sorter.sort(raw_dates)
    print(result)
    single = sorter.sort(['15/05/2020'])
    print(single)