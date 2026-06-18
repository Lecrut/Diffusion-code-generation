def format_time(total_seconds: int) -> str:
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"
if __name__ == '__main__':
    sample_values = [981, 37054, 1]
    for total_seconds in sample_values:
        print(format_time(total_seconds))