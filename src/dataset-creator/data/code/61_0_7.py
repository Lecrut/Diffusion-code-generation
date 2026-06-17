def convert_seconds_to_hm(seconds: int) -> tuple[int, int]:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes
if __name__ == '__main__':
    sample_input = 7265
    h, m = convert_seconds_to_hm(sample_input)
    print(f"{sample_input} seconds is {h} hour(s) and {m} minute(s).")
    if sample_input == 0:
        print("Zero input handled correctly.")