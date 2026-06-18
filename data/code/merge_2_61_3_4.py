def calculate_hours_and_minutes(seconds: int) -> tuple[int, int]:
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    return hours, minutes
if __name__ == '__main__':
    sample_seconds = 9845
    result_hours, result_minutes = calculate_hours_and_minutes(sample_seconds)
    print(f"{result_hours} hours and {result_minutes} minutes")