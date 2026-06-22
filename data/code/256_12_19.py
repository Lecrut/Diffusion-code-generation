from datetime import datetime

def date_range(dates):
    if not dates:
        return None
    start_date = min(map(datetime.strptime, dates, ['%Y-%m-%d'] * len(dates)))
    end_date = max(map(datetime.strptime, dates, ['%Y-%m-%d'] * len(dates)))
    return (end_date - start_date).days

if __name__ == '__main__':
    sample_dates1 = ["2023-01-01", "2023-01-05", "2023-01-03"]
    result1 = date_range(sample_dates1)
    print(f"Range for {sample_dates1}: {result1} days")
    
    sample_dates2 = ["2023-12-25", "2024-01-01"]
    result2 = date_range(sample_dates2)
    print(f"Range for {sample_dates2}: {result2} days")

    sample_dates3 = []
    result3 = date_range(sample_dates3)
    print(f"Range for {sample_dates3}: {result3}")