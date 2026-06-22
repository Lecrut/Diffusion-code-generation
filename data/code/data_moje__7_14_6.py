def seconds_to_dhms(total_seconds):
    total_seconds = int(total_seconds)
    negative = total_seconds < 0
    if negative:
        total_seconds = -total_seconds
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    if negative:
        return (-days, -hours, -minutes, -seconds)
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    sample_values = [0, 86400, 3661, 123456789, -86400, -3661, 1, 60, 3600, 86401]
    for val in sample_values:
        result = seconds_to_dhms(val)
        print(result)