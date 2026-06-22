from datetime import datetime

def date_range(dates):
    if not dates:
        return None
    start_date = min(dates)
    end_date = max(dates)
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    sample_dates1 = ['2023-01-01', '2023-01-15', '2023-01-05']
    dates1 = [datetime.strptime(date, '%Y-%m-%d') for date in sample_dates1]
    result1 = date_range(dates1)
    print(f"Range for {sample_dates1}: {result1} days")

    sample_dates2 = ['2023-02-28', '2023-03-01']
    dates2 = [datetime.strptime(date, '%Y-%m-%d') for date in sample_dates2]
    result2 = date_range(dates2)
    print(f"Range for {sample_dates2}: {result2} days")

    sample_dates3 = ['2023-04-15']
    dates3 = [datetime.strptime(date, '%Y-%m-%d') for date in sample_dates3]
    result3 = date_range(dates3)
    print(f"Range for {sample_dates3}: {result3} days")

    sample_dates4 = []
    result4 = date_range(sample_dates4)
    print(f"Range for empty list: {result4}")