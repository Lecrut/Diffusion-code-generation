def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        return h * 60 + m + s / 60
    except (ValueError, AttributeError):
        raise ValueError("Invalid time format. Please use 'H:M:S'.")
if __name__ == '__main__':
    print(time_to_minutes('2:30:45'))
    print(time_to_minutes('1:15'))