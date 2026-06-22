def hours_to_milliseconds(hours):
    if not isinstance(hours, (int, float)) or hours < 0:
        raise ValueError("Input must be a non-negative number")
    return int(hours * 3600 * 1000)

if __name__ == '__main__':
    sample_hours_1 = 2
    print(f"{sample_hours_1} hours is {hours_to_milliseconds(sample_hours_1)} milliseconds")
    sample_hours_2 = 5
    print(f"{sample_hours_2} hours is {hours_to_milliseconds(sample_hours_2)} milliseconds")