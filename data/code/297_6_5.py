SECONDS_PER_HOUR = 3600
MILLISECONDS_PER_SECOND = 1000

def hours_to_milliseconds(hours):
    return int(hours * SECONDS_PER_HOUR * MILLISECONDS_PER_SECOND)

if __name__ == '__main__':
    sample_hours_1 = 2
    print(f"{sample_hours_1} hours is {hours_to_milliseconds(sample_hours_1)} milliseconds")
    sample_hours_2 = 5
    print(f"{sample_hours_2} hours is {hours_to_milliseconds(sample_hours_2)} milliseconds")