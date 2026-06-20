def seconds_to_dhms(total_seconds):
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    print(seconds_to_dhms(0))
    print(seconds_to_dhms(3661))
    print(seconds_to_dhms(90061))
    print(seconds_to_dhms(86400))
    print(seconds_to_dhms(172800))
    print(seconds_to_dhms(31557600))