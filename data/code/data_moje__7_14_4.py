def seconds_to_dhms(total_seconds):
    if total_seconds < 0:
        raise ValueError("Duration must be non-negative")
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (int(days), int(hours), int(minutes), int(seconds))

if __name__ == '__main__':
    print(seconds_to_dhms(0))
    print(seconds_to_dhms(3661))
    print(seconds_to_dhms(86400))
    print(seconds_to_dhms(3600))
    print(seconds_to_dhms(60))
    print(seconds_to_dhms(1))
    print(seconds_to_dhms(999999999))