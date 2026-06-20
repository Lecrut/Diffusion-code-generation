def seconds_to_minutes(seconds):
    return seconds / 60

def seconds_to_hours(seconds):
    return seconds / 3600

def seconds_to_days(seconds):
    return seconds / 86400

def seconds_to_years(seconds):
    return seconds / 31557600

def seconds_to_months(seconds):
    return seconds / 2629800

def minutes_to_seconds(minutes):
    return minutes * 60

def minutes_to_hours(minutes):
    return minutes / 60

def minutes_to_days(minutes):
    return minutes / 1440

def minutes_to_years(minutes):
    return minutes / 525960

def minutes_to_months(minutes):
    return minutes / 43830

def hours_to_seconds(hours):
    return hours * 3600

def hours_to_minutes(hours):
    return hours * 60

def hours_to_days(hours):
    return hours / 24

def hours_to_years(hours):
    return hours / 8766

def hours_to_months(hours):
    return hours / 730.5

def days_to_seconds(days):
    return days * 86400

def days_to_minutes(days):
    return days * 1440

def days_to_hours(days):
    return days * 24

def days_to_years(days):
    return days / 365.25

def days_to_months(days):
    return days / 30.44

def months_to_seconds(months):
    return months * 2629800

def months_to_minutes(months):
    return months * 43830

def months_to_hours(months):
    return months * 730.5

def months_to_days(months):
    return months * 30.44

def months_to_years(months):
    return months / 12

def years_to_seconds(years):
    return years * 31557600

def years_to_minutes(years):
    return years * 525960

def years_to_hours(years):
    return years * 8766

def years_to_days(years):
    return years * 365.25

def years_to_months(years):
    return years * 12

def convert_time(value, from_unit, to_unit):
    if from_unit == 'seconds':
        if to_unit == 'minutes': return seconds_to_minutes(value)
        elif to_unit == 'hours': return seconds_to_hours(value)
        elif to_unit == 'days': return seconds_to_days(value)
        elif to_unit == 'years': return seconds_to_years(value)
        elif to_unit == 'months': return seconds_to_months(value)
        elif to_unit == 'seconds': return value
    elif from_unit == 'minutes':
        if to_unit == 'seconds': return minutes_to_seconds(value)
        elif to_unit == 'hours': return minutes_to_hours(value)
        elif to_unit == 'days': return minutes_to_days(value)
        elif to_unit == 'years': return minutes_to_years(value)
        elif to_unit == 'months': return minutes_to_months(value)
        elif to_unit == 'minutes': return value
    elif from_unit == 'hours':
        if to_unit == 'seconds': return hours_to_seconds(value)
        elif to_unit == 'minutes': return hours_to_minutes(value)
        elif to_unit == 'days': return hours_to_days(value)
        elif to_unit == 'years': return hours_to_years(value)
        elif to_unit == 'months': return hours_to_months(value)
        elif to_unit == 'hours': return value
    elif from_unit == 'days':
        if to_unit == 'seconds': return days_to_seconds(value)
        elif to_unit == 'minutes': return days_to_minutes(value)
        elif to_unit == 'hours': return days_to_hours(value)
        elif to_unit == 'years': return days_to_years(value)
        elif to_unit == 'months': return days_to_months(value)
        elif to_unit == 'days': return value
    elif from_unit == 'months':
        if to_unit == 'seconds': return months_to_seconds(value)
        elif to_unit == 'minutes': return months_to_minutes(value)
        elif to_unit == 'hours': return months_to_hours(value)
        elif to_unit == 'days': return months_to_days(value)
        elif to_unit == 'years': return months_to_years(value)
        elif to_unit == 'months': return value
    elif from_unit == 'years':
        if to_unit == 'seconds': return years_to_seconds(value)
        elif to_unit == 'minutes': return years_to_minutes(value)
        elif to_unit == 'hours': return years_to_hours(value)
        elif to_unit == 'days': return years_to_days(value)
        elif to_unit == 'months': return years_to_months(value)
        elif to_unit == 'years': return value

if __name__ == '__main__':
    print(convert_time(3600, 'seconds', 'hours'))
    print(convert_time(1, 'hours', 'seconds'))
    print(convert_time(1, 'years', 'days'))
    print(convert_time(1, 'days', 'years'))
    print(convert_time(30, 'days', 'months'))
    print(convert_time(1, 'months', 'days'))
    print(convert_time(1000, 'seconds', 'minutes'))
    print(convert_time(60, 'minutes', 'seconds'))