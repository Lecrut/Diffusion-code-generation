from datetime import timedelta

def get_seconds_in_non_leap_year():
    days_in_year = 365
    if days_in_year <= 0:
        raise ValueError("Days must be positive")
    delta = timedelta(days=days_in_year)
    return delta.total_seconds()

if __name__ == '__main__':
    result = get_seconds_in_non_leap_year()
    print(result)