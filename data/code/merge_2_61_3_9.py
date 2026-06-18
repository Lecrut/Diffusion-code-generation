def convert_seconds_to_hms(seconds: int) -> tuple[int, int]:
    return divmod(seconds, 3600), divmod(divmod(seconds, 3600)[1], 60)
if __name__ == '__main__':
    sample_seconds = 7254
    hours, remaining_minutes = convert_seconds_to_hms(sample_seconds)
    total_hours = int(hours[0]) * 60 + int(hours[1]) if isinstance(hours, tuple) else int(hours)
    final_result: list[int] = [total_hours, sample_seconds % 3600 // 60, sample_seconds % 60]