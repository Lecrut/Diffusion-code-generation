def convert_seconds_to_hours_minutes(total_seconds: int) -> tuple[int, int]:
    return divmod(total_seconds, 3600), divmod(divmod(total_seconds, 3600)[1], 60)
if __name__ == '__main__':
    sample_total = 72540
    hours, minutes = convert_seconds_to_hours_minutes(sample_total)
    print(f"{hours} hours and {minutes} minutes")