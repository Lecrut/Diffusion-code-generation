def minutes_to_days(minutes):
    if not isinstance(minutes, (int, float)) or minutes < 0:
        raise ValueError("Input must be a non-negative number")
    
    conversion_factor = 1 / (24 * 60)
    return minutes * conversion_factor

if __name__ == '__main__':
    sample_minutes = 1440
    print(f"{sample_minutes} minutes is {minutes_to_days(sample_minutes)} days")