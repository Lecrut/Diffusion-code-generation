def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        total_minutes = h * 60 + m + s / 60
        return total_minutes
    except ValueError:
        return None

if __name__ == '__main__':
    sample_time1 = "01:30:45"
    result1 = time_to_minutes(sample_time1)
    print(result1)

    sample_time2 = "14:30:15"
    result2 = time_to_minutes(sample_time2)
    print(result2)