import datetime

def get_days_remaining(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    
    current_date = datetime.date(year, month, day)
    if current_date.month != month:
        raise ValueError("Day out of range for month")
        
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
        
    end_of_month = next_month - datetime.timedelta(days=1)
    remaining = (end_of_month - current_date).days + 1
    return remaining

if __name__ == '__main__':
    results = []
    for y, m, d in [(2023, 2, 15), (2024, 2, 28), (2023, 12, 31)]:
        val = get_days_remaining(y, m, d)
        results.append(val)
    print(results)