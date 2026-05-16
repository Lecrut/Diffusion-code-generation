import datetime
def calculate_duration(date1_str, date2_str, unit):
    date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
    duration = abs(date2 - date1)
    if unit == 'seconds':
        return int(duration.total_seconds())
    elif unit == 'human_readable':
        days = duration.days
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        seconds = duration.seconds % 60
        parts = []
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0:
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
        if not parts:
            return "0 seconds"
        return ", ".join(parts)
    else:
        raise ValueError("Invalid unit specified. Use 'seconds' or 'human_readable'.")
if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2023-01-10"
    print("--- Calculating Duration in Seconds ---")
    seconds_result = calculate_duration(date_a, date_b, 'seconds')
    print(f"Duration between {date_a} and {date_b}: {seconds_result} seconds")
    print("\n--- Calculating Duration in Human-Readable Format ---")
    human_readable_result = calculate_duration(date_a, date_b, 'human_readable')
    print(f"Duration between {date_a} and {date_b}: {human_readable_result}")