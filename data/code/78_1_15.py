from datetime import datetime

def calculate_month_difference(month1, month2):
    year = 2023
    date_format = '%B %Y'
    first_date = datetime.strptime(f'{month1} {year}', date_format)
    second_date = datetime.strptime(f'{month2} {year}', date_format)
    return abs((second_date - first_date).days // 30)
if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))