def seconds_to_dhms(total_seconds):
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    print(seconds_to_dhms(0))
    print(seconds_to_dhms(3661))
    print(seconds_to_dhms(86400))
    print(seconds_to_dhms(90061))
    print(seconds_to_dhms(1000000))