def convert_seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return f"{hours}h {minutes}m {seconds}s"
if __name__ == '__main__':
    sample_values = [3661, 82574, 999]
    for s in sample_values:
        print(f"{s}: {convert_seconds_to_hms(s)}")