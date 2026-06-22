from datetime import date

def days_remaining_in_month(year, month):
    if 1 <= month <= 12:
        _, last_day = calendar.monthrange(year, month)
        today = date.today()
        target_date = date(year, month, last_day)
        return (target_date - today).days
    else:
        raise ValueError("Invalid month")

if __name__ == '__main__':
    print(days_remaining_in_month(2023, 10))