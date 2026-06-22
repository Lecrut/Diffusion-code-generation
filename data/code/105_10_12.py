from datetime import datetime, timedelta

def get_next_day(date_str: str) -> datetime:
    base_date = datetime.strptime(date_str, "%Y-%m-%d")
    return base_date + timedelta(days=1)

if __name__ == '__main__':
    target = '2024-12-31'
    computed = get_next_day(target)
    print(computed)