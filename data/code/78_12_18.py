from datetime import datetime

def calculate_months_difference(date1, date2):
    try:
        d1 = datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.strptime(date2, '%Y-%m-%d')
        months_diff = (d2.year - d1.year) * 12 + (d2.month - d1.month)
        return abs(months_diff)
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    print(calculate_months_difference('2020-01-01', '2023-04-01'))