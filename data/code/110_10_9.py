import datetime

class DateSorter:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def parse_date(date_str):
        try:
            return datetime.datetime.strptime(date_str, DateSorter.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")

    @classmethod
    def sort_date_strings(cls, date_list):
        parsed_dates = [cls.parse_date(date) for date in date_list]
        sorted_dates = sorted(parsed_dates)
        return [sorted_dates.index(date_obj) + 1 for date_obj in parsed_dates]

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2022-12-31', '2023-04-01']
    sorter = DateSorter()
    sorted_indices = sorter.sort_date_strings(sample_dates)
    print(sorted_indices)