from datetime import datetime

def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: datetime.strptime(date, '%m-%d-%Y'))

if __name__ == '__main__':
    dates = ['12-31-2020', '01-01-2021', '07-04-2020', '11-29-2021']
    sorted_dates = sort_date_strings(dates)
    print(sorted_dates)