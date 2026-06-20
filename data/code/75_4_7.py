import datetime

def calculate_days_difference(date1_str, date2_str):
    try:
        format1 = '%m/%d/%Y'
        format2 = '%Y-%m-%d'
        if '/' in date1_str:
            date1 = datetime.datetime.strptime(date1_str, format1)
        else:
            date1 = datetime.datetime.strptime(date1_str, format2)
        if '/' in date2_str:
            date2 = datetime.datetime.strptime(date2_str, format1)
        else:
            date2 = datetime.datetime.strptime(date2_str, format2)
        difference = abs((date2 - date1).days)
        return difference
    except ValueError as e:
        return f'Error: Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD.'
if __name__ == '__main__':
    date1 = '05/23/2021'
    date2 = '2021-06-17'
    result = calculate_days_difference(date1, date2)
    print(result)