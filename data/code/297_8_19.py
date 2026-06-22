def minutes_to_days(minutes):
    if not isinstance(minutes, (int, float)) or minutes < 0:
        raise ValueError("Input must be a non-negative number of minutes.")
    
    return minutes / 1440.0

if __name__ == '__main__':
    sample_minutes = 2880
    print(f"{sample_minutes} minutes is {minutes_to_days(sample_minutes)} days")