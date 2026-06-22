def parse_time(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    total_minutes1 = parse_time(time_str1)
    total_minutes2 = parse_time(time_str2)
    return abs(total_minutes1 - total_minutes2)

if __name__ == '__main__':
    t1 = "09:30"
    t2 = "14:45"
    result = calculate_time_difference(t1, t2)
    print(result)