import sys
def convert_time_to_minutes(hours, minutes, seconds):
    total_minutes = (hours * 60) + minutes + (seconds / 60.0)
    return total_minutes
if __name__ == '__main__':
    sample_hours = 2
    sample_minutes = 30
    sample_seconds = 15
    try:
        hours = int(sample_hours)
        minutes = int(sample_minutes)
        seconds = int(sample_seconds)
        if hours < 0 or minutes < 0 or seconds < 0:
            print("Error: Time components cannot be negative.")
        else:
            total_minutes = convert_time_to_minutes(hours, minutes, seconds)
            print(f"Input Time: {hours} hours, {minutes} minutes, {seconds} seconds")
            print(f"Total minutes: {total_minutes:.2f}")
    except ValueError:
        print("Error: Invalid input. Please ensure all values are integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")