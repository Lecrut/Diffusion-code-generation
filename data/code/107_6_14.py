from datetime import date

DAY_MAP = (
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
)

MONTH_MAP = (
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
)

def format_date(d: date) -> str:
    if not isinstance(d, date):
        raise ValueError("Input must be a date instance")
    day_name = DAY_MAP[d.weekday()]
    month_name = MONTH_MAP[d.month - 1]
    return f"{day_name}, {month_name} {d.day:02d}, {d.year}"

if __name__ == '__main__':
    sample_date = date(2023, 10, 25)
    print(format_date(sample_date))