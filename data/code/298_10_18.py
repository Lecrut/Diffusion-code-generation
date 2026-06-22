from datetime import timedelta

def parse_time(time_str: str) -> tuple[int, int]:
    hours, minutes = map(int, time_str.split(':'))
    if 0 <= hours < 24 and 0 <= minutes < 60:
        return hours, minutes
    raise ValueError("Invalid time format")

def calculate_time_difference(time1: str, time2: str) -> int | None:
    try:
        parsed_time1 = parse_time(time1)
        parsed_time2 = parse_time(time2)
        dt1 = timedelta(hours=parsed_time1[0], minutes=parsed_time1[1])
        dt2 = timedelta(hours=parsed_time2[0], minutes=parsed_time2[1])
        difference = abs(dt2 - dt1)
        return difference.total_seconds() / 60
    except ValueError:
        return None

if __name__ == '__main__':
    time_a = "09:30"
    time_b = "14:45"
    result = calculate_time_difference(time_a, time_b)
    print(f"Time Difference (minutes): {result}")