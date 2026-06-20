import math

CONVERSION_FACTORS = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
    "months": 2629746,
    "years": 31556952,
}

def convert_time(value, from_unit, to_unit):
    if from_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unknown to_unit: {to_unit}")
    
    if from_unit == to_unit:
        return value
    
    value_in_seconds = value * CONVERSION_FACTORS[from_unit]
    converted_value = value_in_seconds / CONVERSION_FACTORS[to_unit]
    
    return converted_value

def calculate_age_in_units(birth_year, birth_month, birth_day):
    import datetime
    now = datetime.datetime.now()
    birth_date = datetime.datetime(birth_year, birth_month, birth_day)
    
    years_diff = now.year - birth_date.year
    months_diff = now.month - birth_date.month
    days_diff = now.day - birth_date.day
    
    if months_diff < 0:
        years_diff -= 1
        months_diff += 12
    if days_diff < 0:
        prev_month = now.month - 1
        if prev_month < 1:
            prev_month = 12
        year_for_prev_month = now.year if now.month > 1 else now.year - 1
        import calendar
        days_in_prev_month = calendar.monthrange(year_for_prev_month, prev_month)[1]
        days_diff += days_in_prev_month
        months_diff -= 1
    
    total_months = (years_diff * 12) + months_diff
    total_days = days_diff
    
    years_in_months = convert_time(total_months, "months", "years")
    days_in_months = convert_time(total_months, "months", "days")
    
    return {
        "years": years_diff,
        "months": months_diff,
        "days": days_diff,
        "total_months_approx": total_months,
        "days_approx_in_months": days_in_months
    }

if __name__ == '__main__':
    result_convert = convert_time(1, "years", "days")
    print(result_convert)
    
    age_data = calculate_age_in_units(1990, 5, 15)
    print(age_data)