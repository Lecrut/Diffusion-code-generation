from datetime import date

def days_remaining_in_month(year, month):
    if 1 <= month <= 12:
        _, last_day = calendar.monthrange(year, month)
        today = date.today()
        return (date(year, month, last_day) - today).days + 1
    else:
        raise ValueError("Invalid month")

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    print(days_remaining_in_month(sample_year, sample_month))