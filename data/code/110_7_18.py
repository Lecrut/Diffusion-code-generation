from datetime import datetime

def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: datetime.strptime(date, '%m-%d-%Y'))

if __name__ == '__main__':
    sample_dates = ['12-31-2020', '01-01-2021', '07-04-2020']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)