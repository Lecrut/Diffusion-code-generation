def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    return hours, minutes
if __name__ == '__main__':
    sample_input = 7265
    result_hours, result_minutes = seconds_to_hm(sample_input)
    print(f"{result_hours}h {result_minutes}m")