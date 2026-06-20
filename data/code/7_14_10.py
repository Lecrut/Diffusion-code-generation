def seconds_to_dhms(total_seconds):
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (int(days), int(hours), int(minutes), int(seconds))

if __name__ == '__main__':
    sample_values = [0, 1, 59, 60, 3600, 3661, 86400, 86461, 99999, 1000000]
    for val in sample_values:
        print(seconds_to_dhms(val))