def time_to_minutes(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 60 + m

if __name__ == '__main__':
    sample_time = "14:30:15"
    result = time_to_minutes(sample_time)
    print(result)