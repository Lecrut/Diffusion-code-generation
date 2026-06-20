def time_to_minutes(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 60 + minutes + seconds / 60
if __name__ == '__main__':
    print(time_to_minutes('1:30:45'))