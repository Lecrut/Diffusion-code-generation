def convert_time_to_duration(total_seconds: int) -> str:
    if total_seconds < 0:
        raise ValueError("Input must be non-negative.")
    seconds = int(total_seconds)
    day_value = seconds // (24 * 60 * 60)
    remainder_after_days = seconds % (24 * 60 * 60)
    hour_value = remainder_after_days // (60 * 60)
    remainder_after_hours = remainder_after_days % (60 * 60)
    minute_value = remainder_after_hours // 60
    second_value = remainder_after_hours % 60
    parts = []
    if day_value > 0:
        suffixes = ['day', 'days'] if day_value != 1 else ''
        parts.append(f"{day_value} {suffixes}")
    if hour_value > 0 or minute_value > 0 or second_value > 0:
        suffixes = ['hour', 'hours'] if hour_value != 1 else ''
        parts.append(f"{hour_value} {suffixes}")
    minutes_str = f"{minute_value} minute" + ('(s)' if minute_value == 1 or (day_value > 0 and hour_value == 0) else '(s)')                                                               
    parts.append(f"{minute_value} minute(s)")
    seconds_str = f"{second_value} second" + ('(s)' if second_value != 1 or day_value > 0 and hour_value == 0 and minute_value == 0 else '(s)')                                                                  
    parts.append(f"{second_value} second(s)")
    return ', '.join(parts)
def main():
    test_cases = [0, 60, 3600, 86400, 172800 + 59 * 60 + 59]
    for sec in test_cases:
        print(f"Input ({sec}) seconds -> {convert_time_to_duration(sec)}")
if __name__ == '__main__':
    main()