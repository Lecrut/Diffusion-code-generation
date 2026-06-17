def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    remaining_after_hours = seconds % 3600
    minutes = remaining_after_hours // 60
    final_seconds = remaining_after_hours % 60
    return f"{hours}h {minutes}m {final_seconds}s"
if __name__ == '__main__':
    sample_input = 98765
    result = convert_seconds_to_hms(sample_input)
    print(result)