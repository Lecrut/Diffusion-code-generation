def convert_duration(total_seconds: int) -> tuple[int, int, int, int]:
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

if __name__ == '__main__':
    total_seconds = 987654
    result = convert_duration(total_seconds)
    print(result)