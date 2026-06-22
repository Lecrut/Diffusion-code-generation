from datetime import datetime

def date_range(date_strings):
    dates = [datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_strings]
    return (min(dates), max(dates))

if __name__ == '__main__':
    sample_dates1 = ['2023-01-01', '2023-01-05', '2023-01-03']
    result1 = date_range(sample_dates1)
    print(f"Range for {sample_dates1}: {result1}")
    
    sample_dates2 = ['2022-12-25', '2023-01-01']
    result2 = date_range(sample_dates2)
    print(f"Range for {sample_dates2}: {result2}")