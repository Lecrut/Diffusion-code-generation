MILLISECONDS_PER_HOUR = 3600 * 1000

def hours_to_milliseconds(hours):
    return int(hours * MILLISECONDS_PER_HOUR)

if __name__ == '__main__':
    sample_hours_1 = 2
    print(f"{sample_hours_1} hours is {hours_to_milliseconds(sample_hours_1)} milliseconds")
    sample_hours_2 = 5
    print(f"{sample_hours_2} hours is {hours_to_milliseconds(sample_hours_2)} milliseconds")