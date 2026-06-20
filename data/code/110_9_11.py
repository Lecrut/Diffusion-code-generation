from datetime import datetime

class DateSorter:
    def __init__(self):
        self.date_formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']

    def normalize_and_sort(self, date_strings):
        normalized_dates = []
        for date_str in date_strings:
            for fmt in self.date_formats:
                try:
                    normalized_date = datetime.strptime(date_str, fmt)
                    normalized_dates.append((normalized_date, date_str))
                    break
                except ValueError:
                    continue
        return [date[1] for date in sorted(normalized_dates)]

if __name__ == '__main__':
    sorter = DateSorter()
    sample_dates = ['2021-03-15', '15/03/2021', '03-15-2021']
    print(sorter.normalize_and_sort(sample_dates))