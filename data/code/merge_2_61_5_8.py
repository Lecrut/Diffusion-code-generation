def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    return divmod(total_seconds, 3600), divmod(total_seconds % 3600, 60)
if __name__ == '__main__':
    sample_total_seconds = 7254
    hours, remainder_minutes = convert_seconds_to_hm(sample_total_seconds)
    minutes, seconds_left = remainder_minutes
    print(f"{sample_total_seconds} seconds is {hours} hour(s), "
          f"{minutes} minute(s), and {seconds_left} second(s).")