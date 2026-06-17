def convert_seconds_to_hms(total_seconds: int) -> tuple[int, int, int]:
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return hours, minutes, seconds
if __name__ == '__main__':
    sample_input = 98451
    h, m, s = convert_seconds_to_hms(sample_input)
    print(f"{h} hours {m} minutes and {s} seconds")