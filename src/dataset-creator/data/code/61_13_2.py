def convert_seconds_to_hms(total_seconds: int) -> str:
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"
if __name__ == '__main__':
    sample_values = [9845, 3701, 12]
    for total_seconds in sample_values:
        print(convert_seconds_to_hms(total_seconds))