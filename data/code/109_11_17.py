import datetime

def calculate_time_remaining(target_month, target_day):
    today = datetime.date.today()
    year = today.year
    if target_month < today.month:
        year += 1
    target_date = datetime.date(year, target_month, target_day)
    remaining_days = (target_date - today).days
    hours = remaining_days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return hours, minutes, seconds

if __name__ == '__main__':
    target_month_1 = 10
    target_day_1 = 25
    hours, minutes, seconds = calculate_time_remaining(target_month_1, target_day_1)
    print(f"Hours remaining: {hours}")
    print(f"Minutes remaining: {minutes}")
    print(f"Seconds remaining: {seconds}")