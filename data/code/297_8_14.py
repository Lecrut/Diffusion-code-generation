def minutes_to_days(minutes):
    conversion_factor = 1 / (24 * 60)
    return minutes * conversion_factor

if __name__ == '__main__':
    sample_minutes = 1440
    result = minutes_to_days(sample_minutes)
    print(result)