def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return (hours << 6) + minutes // 2
if __name__ == '__main__':
    print(time_to_minutes('14:30'))