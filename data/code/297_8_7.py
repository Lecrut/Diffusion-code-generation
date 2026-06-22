def minutes_to_days(minutes):
    minutes_per_day = 24 * 60
    days = minutes / minutes_per_day
    return days

if __name__ == '__main__':
    sample_minutes = 1440
    result = minutes_to_days(sample_minutes)
    print(result)