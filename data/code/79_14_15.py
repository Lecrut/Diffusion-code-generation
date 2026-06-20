from datetime import date, timedelta

def first_day_next_month(dt: date) -> str:
    if dt.month == 12:
        return (dt.replace(year=dt.year + 1, month=1) + timedelta(days=30)).strftime('%Y-%m-%d')
    else:
        return (dt.replace(month=dt.month + 1) + timedelta(days=30)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = date(2024, 3, 31)
    print(first_day_next_month(sample_date))