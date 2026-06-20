def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 | minutes
if __name__ == '__main__':
    print(time_to_minutes('12:34'))
    print(time_to_minutes('09:00'))