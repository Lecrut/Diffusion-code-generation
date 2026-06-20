def validate_time_format(time_str: str) -> None:
    if len(time_str) != 5 or time_str[2] != ':':
        raise ValueError("Invalid time format. Expected HH:MM")

def extract_hours_minutes(time_str: str) -> tuple[int, int]:
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours, minutes

def convert_to_total_minutes(time_str: str) -> int:
    validate_time_format(time_str)
    hours, minutes = extract_hours_minutes(time_str)
    total_minutes = hours * 60 + minutes
    return total_minutes

if __name__ == '__main__':
    time1 = "01:30"
    result1 = convert_to_total_minutes(time1)
    print(f"Time: {time1}, Total Minutes: {result1}")