from datetime import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        return difference
    except ValueError:
        return 'Invalid date format. Please use YYYY-MM-DD.'
if __name__ == '__main__':
    result = calculate_date_difference('2023-04-01', '2023-04-15')
    print(result)