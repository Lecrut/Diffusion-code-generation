from datetime import datetime

def sort_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.strptime(date, '%d/%m/%Y'))

if __name__ == '__main__':
    dates = ['21/03/2020', '15/01/2020', '31/12/2019']
    sorted_dates = sort_dates(dates)
    print(sorted_dates)