import time
def seconds_to_hm(seconds: int) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or float representing seconds.")
    try:
        total_seconds = int(round(float(seconds)))
    except ValueError:
        raise ValueError("Invalid numeric input provided for conversion.")
    hours = total_seconds // 3600
    remaining_minutes = (total_seconds % 3600) // 60
    return hours, remaining_minutes
if __name__ == '__main__':
    sample_input = 7265
    h, m = seconds_to_hm(sample_input)
    print(f"{h} hours and {m} minutes")