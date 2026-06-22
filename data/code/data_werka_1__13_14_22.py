def convert_seconds(duration):
    days = duration // (24 * 3600)
    hours = (duration % (24 * 3600)) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 987654
    days, hours, minutes, seconds = convert_seconds(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")