def time_to_minutes(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    diff = abs(time_to_minutes(time_str2) - time_to_minutes(time_str1))
    return diff if diff <= 720 else 1440 - diff

if __name__ == '__main__':
    time_a = "09:30"
    time_b = "14:45"
    result = calculate_time_difference(time_a, time_b)
    print(result)