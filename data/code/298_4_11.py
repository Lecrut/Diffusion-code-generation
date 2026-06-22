def calculate_duration(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    if start_hour > end_hour or (start_hour == end_hour and start_minute > end_minute):
        end_hour += 24
    total_minutes = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
    return total_minutes

if __name__ == '__main__':
    duration1 = calculate_duration('07:45', '18:23')
    print(f"Duration between 07:45 and 18:23: {duration1} minutes")