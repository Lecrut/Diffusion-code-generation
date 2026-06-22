from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

def calculate_date_range(dates):
    if not dates:
        raise ValueError("Date list cannot be empty")
    parsed_dates = [parse_date(date) for date in dates]
    return (min(parsed_dates), max(parsed_dates))

def get_days_difference(start_date, end_date):
    return (end_date - start_date).days

if __name__ == '__main__':
    sample_dates1 = ['2023-01-01', '2023-02-01', '2023-03-01']
    range1 = calculate_date_range(sample_dates1)
    print(f"Date range for {sample_dates1}: {range1}")
    days_diff1 = get_days_difference(range1[0], range1[1])
    print(f"Days difference: {days_diff1}")

    sample_dates2 = ['2023-12-25', '2024-01-01']
    range2 = calculate_date_range(sample_dates2)
    print(f"Date range for {sample_dates2}: {range2}")
    days_diff2 = get_days_difference(range2[0], range2[1])
    print(f"Days difference: {days_diff2}")

    sample_dates3 = ['2023-07-04']
    try:
        range3 = calculate_date_range(sample_dates3)
        print(f"Date range for {sample_dates3}: {range3}")
    except ValueError as e:
        print(e)

    sample_dates4 = []
    try:
        range4 = calculate_date_range(sample_dates4)
        print(f"Date range for {sample_dates4}: {range4}")
    except ValueError as e:
        print(e)