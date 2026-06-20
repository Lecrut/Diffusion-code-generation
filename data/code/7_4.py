def convert_time(value, from_unit, to_unit):
    base_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2629746,
        'years': 31556952
    }
    
    if from_unit not in base_seconds or to_unit not in base_seconds:
        raise ValueError("Unsupported time unit provided")
    
    value_in_seconds = value * base_seconds[from_unit]
    converted_value = value_in_seconds / base_seconds[to_unit]
    
    return converted_value

def create_time_context(value, unit):
    seconds_total = convert_time(value, unit, 'seconds')
    
    years = int(seconds_total / 31556952)
    remaining_seconds = seconds_total - (years * 31556952)
    
    months = int(remaining_seconds / 2629746)
    remaining_seconds = remaining_seconds - (months * 2629746)
    
    weeks = int(remaining_seconds / 604800)
    remaining_seconds = remaining_seconds - (weeks * 604800)
    
    days = int(remaining_seconds / 86400)
    remaining_seconds = remaining_seconds - (days * 86400)
    
    hours = int(remaining_seconds / 3600)
    remaining_seconds = remaining_seconds - (hours * 3600)
    
    minutes = int(remaining_seconds / 60)
    remaining_seconds = remaining_seconds - (minutes * 60)
    
    seconds = int(remaining_seconds)
    
    return {
        'years': years,
        'months': months,
        'weeks': weeks,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

if __name__ == '__main__':
    result = convert_time(1, 'years', 'days')
    print(result)
    
    detailed_breakdown = create_time_context(365, 'days')
    print(detailed_breakdown)