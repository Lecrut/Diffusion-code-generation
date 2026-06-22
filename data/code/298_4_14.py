def calculate_duration(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    
    total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)
    return total_minutes

if __name__ == '__main__':
    duration = calculate_duration('07:45', '18:23')
    print(duration)