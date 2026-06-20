def duration_to_minutes(duration_str):
    hours, minutes, _ = map(int, duration_str.split(':'))
    return hours * 60 + minutes
if __name__ == '__main__':
    print(duration_to_minutes('1:30:00'))