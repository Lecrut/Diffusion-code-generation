from datetime import datetime

def calculate_difference(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%m/%d/%Y')
        date2 = datetime.strptime(date_str2, '%m/%d/%Y')
        return abs((date2 - date1).days)
    except ValueError as e:
        print(f'Invalid date format: {e}')
        return None
if __name__ == '__main__':
    sample_date1 = '05/23/2023'
    sample_date2 = '06/10/2023'
    difference = calculate_difference(sample_date1, sample_date2)
    print(difference)