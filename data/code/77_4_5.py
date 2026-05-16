import sys
def convert_to_minutes(hours, minutes, seconds):
    total_minutes = (hours * 60) + minutes + (seconds / 60.0)
    return total_minutes
if __name__ == '__main__':
    sample_hours = 2
    sample_minutes = 30
    sample_seconds = 15
    try:
        print(f"Sample Input: Hours={sample_hours}, Minutes={sample_minutes}, Seconds={sample_seconds}")
        total_minutes = convert_to_minutes(sample_hours, sample_minutes, sample_seconds)
        print(f"Total minutes: {total_minutes}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)