TIME_FORMAT = "%H:%M"

def time_to_minutes(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    return abs(time_to_minutes(time_str1) - time_to_minutes(time_str2))

if __name__ == '__main__':
    time_a = "09:30"
    time_b = "14:45"
    difference = calculate_time_difference(time_a, time_b)
    print(f"Time difference in minutes: {difference}")