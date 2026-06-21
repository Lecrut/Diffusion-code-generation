from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def sort_dates_chronologically(date_list):
    if not date_list:
        return []
    def convert_to_datetime(date_str):
        return datetime.strptime(date_str, DATE_FORMAT)
    return sorted(date_list, key=convert_to_datetime)

if __name__ == '__main__':
    input_dates = ['2024-01-15', '2020-12-25', '2023-06-01', '2021-03-10']
    ordered_dates = sort_dates_chronologically(input_dates)
    print(ordered_dates)