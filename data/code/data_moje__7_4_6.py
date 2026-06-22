def years_to_days(years):
    return years * 365.25

def days_to_years(days):
    return days / 365.25

def months_to_days(months):
    return months * (365.25 / 12)

def days_to_months(days):
    return days / (365.25 / 12)

def days_to_hours(days):
    return days * 24

def hours_to_days(hours):
    return hours / 24

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60

def minutes_to_seconds(minutes):
    return minutes * 60

def seconds_to_minutes(seconds):
    return seconds / 60

def hours_to_seconds(hours):
    return hours * 3600

def seconds_to_hours(seconds):
    return seconds / 3600

def days_to_seconds(days):
    return days * 86400

def seconds_to_days(seconds):
    return seconds / 86400

def months_to_hours(months):
    return months_to_days(months) * 24

def hours_to_months(hours):
    return hours_to_days(hours) / (365.25 / 12)

def months_to_minutes(months):
    return months_to_hours(months) * 60

def minutes_to_months(minutes):
    return minutes_to_hours(minutes) / (365.25 / 12)

def months_to_seconds(months):
    return months_to_hours(months) * 3600

def seconds_to_months(seconds):
    return seconds_to_hours(seconds) / (365.25 / 12)

def years_to_hours(years):
    return years_to_days(years) * 24

def hours_to_years(hours):
    return hours_to_days(hours) / 365.25

def years_to_minutes(years):
    return years_to_hours(years) * 60

def minutes_to_years(minutes):
    return minutes_to_hours(minutes) / 365.25

def years_to_seconds(years):
    return years_to_hours(years) * 3600

def seconds_to_years(seconds):
    return seconds_to_hours(seconds) / 365.25

if __name__ == '__main__':
    print(years_to_days(1))
    print(days_to_years(365.25))
    print(months_to_days(1))
    print(days_to_months(30.4375))
    print(days_to_hours(1))
    print(hours_to_days(24))
    print(hours_to_minutes(1))
    print(minutes_to_hours(60))
    print(minutes_to_seconds(1))
    print(seconds_to_minutes(60))
    print(hours_to_seconds(1))
    print(seconds_to_hours(3600))
    print(days_to_seconds(1))
    print(seconds_to_days(86400))
    print(months_to_hours(1))
    print(hours_to_months(730.5))
    print(months_to_minutes(1))
    print(minutes_to_months(43830))
    print(months_to_seconds(1))
    print(seconds_to_months(2629800))
    print(years_to_hours(1))
    print(hours_to_years(8766))
    print(years_to_minutes(1))
    print(minutes_to_years(525960))
    print(years_to_seconds(1))
    print(seconds_to_years(31557600))