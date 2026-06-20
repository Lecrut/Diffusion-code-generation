def _days_to_seconds(days):
    return days * 24 * 60 * 60

def _years_to_days(years):
    return years * 365.25

def _months_to_days(months):
    return months * 30.4375

def convert_time(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if value < 0:
        raise ValueError("Value must be non-negative")
    
    to_seconds = 0
    
    if from_unit == 'seconds':
        to_seconds = value
    elif from_unit == 'minutes':
        to_seconds = value * 60
    elif from_unit == 'hours':
        to_seconds = value * 3600
    elif from_unit == 'days':
        to_seconds = value * 86400
    elif from_unit == 'weeks':
        to_seconds = value * 86400 * 7
    elif from_unit == 'months':
        to_seconds = _months_to_days(value) * 86400
    elif from_unit == 'years':
        to_seconds = _years_to_days(value) * 86400
    else:
        raise ValueError(f"Unknown source unit: {from_unit}")
    
    if to_unit == 'seconds':
        return to_seconds
    elif to_unit == 'minutes':
        return to_seconds / 60
    elif to_unit == 'hours':
        return to_seconds / 3600
    elif to_unit == 'days':
        return to_seconds / 86400
    elif to_unit == 'weeks':
        return to_seconds / (86400 * 7)
    elif to_unit == 'months':
        return to_seconds / (86400 * 30.4375)
    elif to_unit == 'years':
        return to_seconds / (86400 * 365.25)
    else:
        raise ValueError(f"Unknown target unit: {to_unit}")

def main():
    years_in_a_day = convert_time(1, 'days', 'years')
    seconds_in_a_year = convert_time(1, 'years', 'seconds')
    minutes_in_a_week = convert_time(1, 'weeks', 'minutes')
    
    print(f"1 day in years: {years_in_a_day}")
    print(f"1 year in seconds: {seconds_in_a_year}")
    print(f"1 week in minutes: {minutes_in_a_week}")

if __name__ == '__main__':
    main()