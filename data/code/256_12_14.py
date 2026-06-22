import datetime

def date_range(dates):
    if not dates:
        return None
    start_date = min(dates)
    end_date = max(dates)
    return (end_date - start_date).days

if __name__ == '__main__':
    sample_dates1 = ['2023-01-01', '2023-02-01', '2023-03-01']
    result1 = date_range([datetime.date.fromisoformat(d) for d in sample_dates1])
    print(f"Range for {sample_dates1}: {result1} days")
    
    sample_dates2 = ['2023-04-15', '2023-06-20', '2023-07-10']
    result2 = date_range([datetime.date.fromisoformat(d) for d in sample_dates2])
    print(f"Range for {sample_dates2}: {result2} days")
    
    sample_dates3 = []
    result3 = date_range(sample_dates3)
    print(f"Range for {sample_dates3}: {result3}")