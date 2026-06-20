from datetime import datetime

def sort_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.strptime(date, '%d/%m/%Y'))

if __name__ == '__main__':
    dates = ['23/04/2021', '01/01/2020', '15/12/2021']
    sorted_dates = sort_dates(dates)
    print(sorted_dates)