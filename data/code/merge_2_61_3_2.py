def calculate_time(seconds: int) -> tuple[int, int]:
    return divmod(seconds, 3600), divmod(divmod(seconds, 3600)[1], 60)
if __name__ == '__main__':
    sample_seconds = 7265
    hours, remaining_minutes = calculate_time(sample_seconds)
    minutes, seconds_left = remaining_minutes
    print(f"{hours}h {minutes}m")