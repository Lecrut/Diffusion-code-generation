from datetime import datetime

DATE_FORMAT = '%d/%m/%Y'

def sort_dates(date_strings):
    if not date_strings:
        return []
    def parse_date(ds):
        return datetime.strptime(ds, DATE_FORMAT)
    return sorted(date_strings, key=parse_date)

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)