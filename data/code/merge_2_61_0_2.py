def convert_seconds(seconds: int) -> tuple[int, int]:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes
if __name__ == '__main__':
    sample_input = 7265
    h, m = convert_seconds(sample_input)
    print(f"{h} hours and {m} minutes")