def minutes_to_days(minutes):
    if not isinstance(minutes, (int, float)) or minutes < 0:
        raise ValueError("Invalid input: Minutes must be a non-negative number")
    return minutes / 1440.0

if __name__ == '__main__':
    print(minutes_to_days(2880))
    print(minutes_to_days(720))