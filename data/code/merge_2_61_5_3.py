def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    hours = total_seconds // 3600
    remaining_after_hours = (total_seconds % 3600) // 60
    minutes = remaining_after_hours
    return hours, minutes
if __name__ == '__main__':
    sample_total_seconds = 7265
    h, m = convert_seconds_to_hm(sample_total_seconds)
    print(f"{h} hours and {m} minutes")