from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        return min(datetime.strptime(date_str1, '%Y-%m-%d'), datetime.strptime(date_str2, '%Y-%m-%d'))
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return None

if __name__ == '__main__':
    earlier_date = compare_dates('2023-04-15', '2023-03-20')
    if earlier_date is not None:
        print(earlier_date)