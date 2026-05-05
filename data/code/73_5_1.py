from datetime import datetime
def calculate_duration(date1_str, date2_str, unit):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    time_difference = abs(date2 - date1)
    if unit == 'seconds':
        return int(time_difference.total_seconds())
    elif unit == 'human_readable':
        days = time_difference.days
        hours = time_difference.seconds // 3600
        minutes = (time_difference.seconds % 3600) // 60
        seconds = time_difference.seconds % 60
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
        raise ValueError("Invalid unit specified. Must be 'seconds' or 'human_readable'.")
if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2023-01-10"
    print("--- Calculating duration in seconds ---")
    seconds_result = calculate_duration(date_a, date_b, 'seconds')
    print(f"Duration between {date_a} and {date_b}: {seconds_result} seconds")
    print("\n--- Calculating duration in human-readable format ---")
    human_readable_result = calculate_duration(date_a, date_b, 'human_readable')
    print(f"Duration between {date_a} and {date_b}: {human_readable_result}")