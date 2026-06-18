def calculate_time_from_seconds(total_seconds: int) -> tuple[int, int]:
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Input must be an integer representing seconds.")
    return divmod(int(round(total_seconds)), 3600), divmod(divmod(int(round(total_seconds)), 3600)[1], 60)
if __name__ == '__main__':
    sample_input = 7254
    hours, minutes = calculate_time_from_seconds(sample_input)
    print(f"{hours} hours and {minutes} minutes")