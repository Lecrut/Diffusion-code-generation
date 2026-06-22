import calendar
from datetime import date

def get_days_of_month(date_strings):
    if not isinstance(date_strings, (list, tuple)):
        raise ValueError("Input must be a list or tuple of strings")
    days = []
    for ds in date_strings:
        if not isinstance(ds, str):
            raise ValueError(f"Expected string, got {type(ds).__name__}")
        if len(ds) != 10 or ds[4] != '-' or ds[7] != '-':
            raise ValueError(f"Invalid format: {ds}")
        try:
            y = int(ds[0:4])
            m = int(ds[5:7])
            d = int(ds[8:10])
        except ValueError:
            raise ValueError(f"Invalid date components in: {ds}")
        max_day = calendar.monthrange(y, m)[1]
        if d < 1 or d > max_day:
            raise ValueError(f"Day out of range for {ds}")
        days.append(d)
    return days

if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-02-29", "2025-12-31"]
    result = get_days_of_month(sample_dates)
    print(result)