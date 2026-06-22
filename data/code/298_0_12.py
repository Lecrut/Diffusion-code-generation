MINUTES_TO_HOURS = 60

def time_to_minutes(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * MINUTES_TO_HOURS + minutes

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    min1 = time_to_minutes(time_str1)
    min2 = time_to_minutes(time_str2)
    diff = abs(min1 - min2)
    return diff // MINUTES_TO_HOURS
if __name__ == '__main__':
    t1 = '09:30'
    t2 = '14:45'
    result = calculate_time_difference(t1, t2)
    print(result)