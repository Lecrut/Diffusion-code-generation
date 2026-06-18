def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    return divmod(total_seconds, 3600), divmod(divmod(total_seconds, 3600)[1], 60)
if __name__ == '__main__':
    sample_total = 7254
    hours, remaining_minutes = convert_seconds_to_hm(sample_total)
    print(f"{sample_total} seconds is {hours} hour(s) and {remaining_minutes[0]} minute(s)")