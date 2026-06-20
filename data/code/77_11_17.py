def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        return h * 60 + m + (s / 60)
    except ValueError:
        raise ValueError("Invalid time format. Expected 'HH:MM:SS'.")

if __name__ == '__main__':
    sample_time = "12:34:56"
    minutes = time_to_minutes(sample_time)
    print(minutes)