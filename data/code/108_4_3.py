import calendar

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def verify_date(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    
    days_in_month = calendar.monthrange(year, month)[1]
    if day > days_in_month:
        raise ValueError("Day exceeds days in month")
    
    weekday_index = calendar.weekday(year, month, day)
    weekday_name = DAY_NAMES[weekday_index]
    
    return {
        "year": year,
        "month": month,
        "day": day,
        "weekday": weekday_name,
        "is_valid": True
    }

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    result = verify_date(sample_year, sample_month, sample_day)
    print(result)