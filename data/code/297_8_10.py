MINUTES_PER_DAY = 1440

def minutes_to_days(minutes):
    return minutes / MINUTES_PER_DAY

if __name__ == '__main__':
    sample_minutes = 2880
    print(minutes_to_days(sample_minutes))