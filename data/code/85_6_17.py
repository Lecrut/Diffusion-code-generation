import datetime

def calculate_week_difference(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
        diff = abs((date1 - date2).days)
        weeks = diff // 7
        return weeks
    except ValueError as e:
        print(f"Invalid date format: {e}")
        raise

if __name__ == '__main__':
    sample_date1 = '2023-01-01'
    sample_date2 = '2023-04-01'
    result = calculate_week_difference(sample_date1, sample_date2)
    print(result)