def determine_leap_status(year):
    thresholds = {
        400: True,
        100: False,
        4: True
    }
    for divisor, is_leap in thresholds.items():
        if year % divisor == 0:
            return is_leap
    return False

if __name__ == '__main__':
    print(determine_leap_status(2000))
    print(determine_leap_status(1900))
    print(determine_leap_status(2024))