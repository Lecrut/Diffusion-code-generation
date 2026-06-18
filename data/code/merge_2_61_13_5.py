def convert_seconds_to_hms(total_seconds: int) -> str:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"
if __name__ == '__main__':
    sample_inputs = [
        1, 
        90, 
        3700, 
        86400,
        91537
    ]
    for seconds in sample_inputs:
        print(convert_seconds_to_hms(seconds))