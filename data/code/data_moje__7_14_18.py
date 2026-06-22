def seconds_to_components(total_seconds: int) -> tuple:
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    duration = 90061
    result = seconds_to_components(duration)
    print(result)