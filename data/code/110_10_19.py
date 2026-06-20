from datetime import datetime

def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date_str: datetime.strptime(date_str, '%Y-%m-%d'))

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2022-12-31', '2023-04-01']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)