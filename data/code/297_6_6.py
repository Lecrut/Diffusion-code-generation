def hours_to_milliseconds(hours):
    seconds_per_hour = 3600
    milliseconds_per_second = 1000
    total_milliseconds = int(hours * seconds_per_hour * milliseconds_per_second)
    return total_milliseconds

if __name__ == '__main__':
    sample_hours_1 = 3
    print(f"{sample_hours_1} hours is {hours_to_milliseconds(sample_hours_1)} milliseconds")
    sample_hours_2 = 7
    print(f"{sample_hours_2} hours is {hours_to_milliseconds(sample_hours_2)} milliseconds")