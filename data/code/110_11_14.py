from datetime import datetime

class DateSorter:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def sort_dates(date_strings):
        date_objects = [datetime.strptime(date_str, DateSorter.DATE_FORMAT) for date_str in date_strings]
        sorted_date_objects = sorted(date_objects)
        return [dt.strftime(DateSorter.DATE_FORMAT) for dt in sorted_date_objects]

if __name__ == '__main__':
    sample_dates = ["2023-10-26", "2023-10-25", "2023-10-27", "2023-10-24"]
    sorted_result = DateSorter.sort_dates(sample_dates)
    print(sorted_result)