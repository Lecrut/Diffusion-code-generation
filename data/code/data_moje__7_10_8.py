def convert_time_duration(amount, unit):
    valid_units = {'seconds', 'minutes', 'hours', 'days'}
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Must be one of {valid_units}")
    
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Amount must be a non-negative number")

    factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }

    total_seconds = amount * factors[unit]

    result = {
        'seconds': total_seconds,
        'minutes': total_seconds / 60,
        'hours': total_seconds / 3600,
        'days': total_seconds / 86400
    }
    
    return result

if __name__ == '__main__':
    sample_amount = 2.5
    sample_unit = 'hours'
    output = convert_time_duration(sample_amount, sample_unit)
    print(f"Input: {sample_amount} {sample_unit}")
    print(f"Seconds: {output['seconds']}")
    print(f"Minutes: {output['minutes']}")
    print(f"Hours: {output['hours']}")
    print(f"Days: {output['days']}")