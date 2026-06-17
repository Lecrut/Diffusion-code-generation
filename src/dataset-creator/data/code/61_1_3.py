def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    hours = total_seconds // 3600
    remaining_after_hours = (total_seconds % 3600) // 60
    minutes = remaining_after_hours
    return hours, minutes
if __name__ == '__main__':
    sample_input: int = 7265
    result: tuple[int, int] = seconds_to_hm(sample_input)
    print(f"{sample_input} seconds is {result[0]} hours and {result[1]} minutes.")