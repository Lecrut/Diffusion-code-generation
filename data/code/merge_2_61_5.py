def convert_seconds_to_time(total_seconds: int) -> tuple[int, int]:
    return divmod(total_seconds, 3600), divmod(divmod(total_seconds, 3600)[1], 60)
if __name__ == '__main__':
    sample_total = 7254
    hours, (minutes, seconds_remainder) = convert_seconds_to_time(sample_total)
    print(f"{hours}h {minutes}m")