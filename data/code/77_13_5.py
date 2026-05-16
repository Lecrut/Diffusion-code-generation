import sys
def convert_to_minutes(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Incorrect format")
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
            raise ValueError("Time components out of valid range")
        total_minutes = hours * 60 + minutes + seconds
        return total_minutes
    except ValueError as e:
        sys.stderr.write(f"Error: Invalid time format or value. {e}\n")
        return None
if __name__ == '__main__':
    sample_times = [
        "0:0:0",
        "23:59:59",
        "10:30:15",
        "25:0:0",
        "1:70:0",
        "10:30"
    ]
    for time_str in sample_times:
        result = convert_to_minutes(time_str)
        if result is not None:
            print(f"Input: {time_str}, Total Minutes: {result}")
        print("-" * 20)