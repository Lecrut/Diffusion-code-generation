from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return min(date1, date2)
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return None

if __name__ == '__main__':
    earlier_date = compare_dates('2023-04-01', '2023-03-15')
    if earlier_date is not None:
        print(earlier_date)