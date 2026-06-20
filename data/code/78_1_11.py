from datetime import datetime

def calculate_month_difference(month1, month2):
    year = 2023
    date_format = '%B'
    first_date = datetime.strptime(f'{month1} {year}', date_format)
    second_date = datetime.strptime(f'{month2} {year}', date_format)
    difference = abs((second_date.year - first_date.year) * 12 + second_date.month - first_date.month)
    return difference
if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))