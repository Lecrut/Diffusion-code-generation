from datetime import datetime

def sort_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.strptime(date, '%d/%m/%Y'))

if __name__ == '__main__':
    dates = ['12/05/2023', '01/01/2023', '15/08/2023']
    sorted_dates = sort_dates(dates)
    print(sorted_dates)