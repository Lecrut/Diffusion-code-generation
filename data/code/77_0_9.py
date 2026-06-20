def time_to_minutes(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 60 + minutes

if __name__ == '__main__':
    sample_time = "02:45:30"
    result = time_to_minutes(sample_time)
    print(result)