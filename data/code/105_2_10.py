from datetime import datetime, timedelta

def get_next_friday(ref_date):
    days_ahead = (4 - ref_date.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    return ref_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    ref = datetime(2023, 12, 15)
    ans = get_next_friday(ref)
    print(ans.strftime('%Y-%m-%d'))