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
        total_minutes = (hours * 60) + minutes + (seconds / 60.0)
        return total_minutes
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_time = "1:30:45"
    result = convert_to_minutes(sample_time)
    print(result)