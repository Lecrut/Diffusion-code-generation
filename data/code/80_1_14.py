from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        return min(datetime.strptime(date_str1, '%Y-%m-%d'), datetime.strptime(date_str2, '%Y-%m-%d'))
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return None

if __name__ == '__main__':
    date1 = '2023-04-01'
    date2 = '2023-03-15'
    earlier_date = compare_dates(date1, date2)
    print(earlier_date)