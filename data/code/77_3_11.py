def time_to_minutes(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 60 + minutes + seconds / 60
    except ValueError:
        raise ValueError("Invalid time format. Please use 'H:M:S'.")
if __name__ == '__main__':
    print(time_to_minutes('2:30:45'))
    print(time_to_minutes('1:15'))