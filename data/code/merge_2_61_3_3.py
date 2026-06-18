def calculate_hours_minutes(seconds: int) -> tuple[int, int]:
    return divmod(seconds, 3600), (seconds % 3600) // 60
if __name__ == '__main__':
    sample_seconds = 7254
    total_hours, remaining_minutes = calculate_hours_minutes(sample_seconds)
    print(f"Hours: {total_hours}")
    print("Minutes: " + str(remaining_minutes))