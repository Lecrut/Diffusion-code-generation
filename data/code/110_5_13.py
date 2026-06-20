from datetime import datetime

class DateSorter:
    DATE_FORMAT = '%d/%m/%Y'

    @staticmethod
    def sort_dates(date_strings):
        parsed_dates = []
        for date_str in date_strings:
            try:
                date_obj = datetime.strptime(date_str, DateSorter.DATE_FORMAT)
                parsed_dates.append(date_obj)
            except ValueError:
                continue
        parsed_dates.sort()
        return [date.strftime(DateSorter.DATE_FORMAT) for date in parsed_dates]

if __name__ == '__main__':
    sample_dates = [
        "20/12/2023",
        "15/11/2023",
        "01/01/2024",
        "10/10/2023"
    ]
    sorted_dates = DateSorter.sort_dates(sample_dates)
    print(sorted_dates)