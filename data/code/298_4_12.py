def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def calculate_duration(start_time, end_time):
    start_minutes = parse_time(start_time)
    end_minutes = parse_time(end_time)
    if start_minutes > end_minutes:
        end_minutes += 24 * 60
    return (end_minutes - start_minutes) // 60

if __name__ == '__main__':
    result = calculate_duration('07:45', '18:23')
    print(result)