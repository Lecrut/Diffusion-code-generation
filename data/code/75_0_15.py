from datetime import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    try:
        date_obj1 = datetime.strptime(date_str1, date_format)
        date_obj2 = datetime.strptime(date_str2, date_format)
    except ValueError:
        date_format = '%d/%m/%Y'
        try:
            date_obj1 = datetime.strptime(date_str1, date_format)
            date_obj2 = datetime.strptime(date_str2, date_format)
        except ValueError:
            raise ValueError('Invalid date format. Please use YYYY-MM-DD or DD/MM/YYYY.')
    difference = abs((date_obj2 - date_obj1).days)
    return difference
if __name__ == '__main__':
    result = calculate_date_difference('2023-10-05', '2023-10-12')
    print(result)