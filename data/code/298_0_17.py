def parse_time(time_str: str) -> int:
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    time1 = parse_time(time_str1)
    time2 = parse_time(time_str2)
    diff = abs(time1 - time2)
    return diff // 60

if __name__ == '__main__':
    t1 = "09:30"
    t2 = "14:45"
    result = calculate_time_difference(t1, t2)
    print(result)