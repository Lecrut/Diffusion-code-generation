import sys
def convert_time_to_minutes(hours, minutes, seconds):
    total_minutes = hours * 60 + minutes + seconds / 60
    return total_minutes
if __name__ == '__main__':
    sample_input = "1:30:15"
    try:
        parts = sample_input.split(':')
        if len(parts) != 3:
            print("Error: Input format must be 'Hours:Minutes:Seconds'.")
            sys.exit(1)
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        if hours < 0 or minutes < 0 or seconds < 0:
            print("Error: Time components cannot be negative.")
            sys.exit(1)
        result = convert_time_to_minutes(hours, minutes, seconds)
        print(f"{result}")
    except ValueError:
        print("Error: All parts of the input must be valid integers.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)