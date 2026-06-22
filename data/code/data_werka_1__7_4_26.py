def seconds_to_minutes(seconds):
    return seconds / 60

def minutes_to_seconds(minutes):
    return minutes * 60

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60

def days_to_hours(days):
    return days * 24

def hours_to_days(hours):
    return hours / 24

def weeks_to_days(weeks):
    return weeks * 7

def days_to_weeks(days):
    return days / 7

def months_to_days(months):
    return months * 30.44

def days_to_months(days):
    return days / 30.44

def years_to_days(years):
    return years * 365.25

def days_to_years(days):
    return days / 365.25
if __name__ == '__main__':
    print(seconds_to_minutes(180))
    print(minutes_to_seconds(3))
    print(hours_to_minutes(2))
    print(minutes_to_hours(120))
    print(days_to_hours(7))
    print(hours_to_days(168))
    print(weeks_to_days(4))
    print(days_to_weeks(28))
    print(months_to_days(12))
    print(days_to_months(365.28))
    print(years_to_days(1))
    print(days_to_years(365.25))