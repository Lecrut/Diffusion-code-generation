def calculate_hours_and_minutes(total_seconds: int) -> tuple[int, int]:
    return divmod(total_seconds, 3600), (total_seconds // 60) % 60
if __name__ == '__main__':
    sample_seconds = 7254
    hours, minutes = calculate_hours_and_minutes(sample_seconds)
    print(f"{hours} hours and {minutes} minutes")