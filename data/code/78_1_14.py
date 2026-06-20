from datetime import date

def calculate_month_difference(month1, month2):
    year = 2023
    first_date = date(year, list(date.month_name).index(month1), 1)
    second_date = date(year, list(date.month_name).index(month2), 1)
    return abs((second_date - first_date).days // 30)
if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))