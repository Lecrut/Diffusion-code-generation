def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    return total_seconds // 3600, (total_seconds % 3600) // 60
if __name__ == '__main__':
    sample_total = 7265
    hours, minutes = convert_seconds_to_hm(sample_total)
    print(f"{hours}h {minutes}m")