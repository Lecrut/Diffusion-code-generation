from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def calculate_date_difference(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, DATE_FORMAT)
    date2 = datetime.strptime(date2_str, DATE_FORMAT)
    return abs((date2 - date1).days)
if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2023-01-10'
    difference = calculate_date_difference(date1, date2)
    print(difference)