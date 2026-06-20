def time_to_minutes(time_str: str) -> int:
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    total_minutes = hours * 60 + minutes
    return total_minutes

if __name__ == '__main__':
    sample_time = "23:45"
    result = time_to_minutes(sample_time)
    print(f"Time: {sample_time}, Total Minutes: {result}")