def convert_to_total_minutes(time_str: str) -> int:
    parts = time_str.split(':')
    if len(parts) != 2:
        raise ValueError("Invalid time format. Expected HH:MM")
    hours = int(parts[0])
    minutes = int(parts[1])
    total_minutes = hours * 60 + minutes
    return total_minutes

if __name__ == '__main__':
    sample_time1 = "08:45"
    result1 = convert_to_total_minutes(sample_time1)
    print(f"Time: {sample_time1}, Total Minutes: {result1}")

    sample_time2 = "23:15"
    result2 = convert_to_total_minutes(sample_time2)
    print(f"Time: {sample_time2}, Total Minutes: {result2}")