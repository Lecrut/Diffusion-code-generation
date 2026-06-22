from datetime import datetime

def date_range(date1, date2):
    return abs((datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(date1, '%Y-%m-%d')).days)

if __name__ == '__main__':
    print(date_range('2023-01-01', '2023-01-31'))