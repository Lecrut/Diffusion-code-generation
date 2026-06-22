from datetime import date

def fraction_month_remaining(start_date: date, end_date: date) -> float:
    total_days = (end_date - start_date).days
    if total_days <= 0:
        return 0.0
    remaining_days = (end_date - date.today()).days
    if remaining_days < 0:
        remaining_days = 0
    if remaining_days > total_days:
        remaining_days = total_days
    return remaining_days / total_days

if __name__ == '__main__':
    start = date(2023, 1, 1)
    end = date(2023, 12, 31)
    result = fraction_month_remaining(start, end)
    print(result)