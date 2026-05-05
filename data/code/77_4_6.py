import sys
def convert_time_to_minutes(hours, minutes, seconds):
    total_minutes = (hours * 60) + minutes + (seconds / 60.0)
    return total_minutes
if __name__ == '__main__':
    sample_hours = 2
    sample_minutes = 30
    sample_seconds = 15
    total_minutes = convert_time_to_minutes(sample_hours, sample_minutes, sample_seconds)
    print(f"Sample Input: {sample_hours} hours, {sample_minutes} minutes, {sample_seconds} seconds")
    print(f"Total minutes: {total_minutes}")