def seconds_to_dhms(total_seconds):
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    sample_values = [0, 1, 59, 60, 3599, 3600, 86399, 86400, 86401, 99999, 31536000, 31536001]
    for val in sample_values:
        print(seconds_to_dhms(val))