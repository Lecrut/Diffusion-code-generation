def convert_time_to_seconds(total_seconds):
    if not isinstance(total_seconds, int):
        raise TypeError("Input must be an integer.")
    if total_seconds < 0:
        raise ValueError("Time cannot be negative.")
    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }
def main():
    time_1 = convert_time_to_seconds(3600)
    large_input = int("9" * 50)                        
    print(f"Input: {time_1}")
    result_large = convert_time_to_seconds(large_input)
    total_days_str = str(result_large['days']) + " days, "\
                    f"{result_large['hours']} hours, "\
                    f"{result_large['minutes']} minutes, and "\
                    f"{result_large['seconds']} seconds"
    print(f"Large Input ({len(str(large_input))} digits): {total_days_str}")
if __name__ == '__main__':
    main()