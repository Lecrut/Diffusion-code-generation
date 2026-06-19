def convert_seconds(duration):
    days = duration // (3600 * 24)
    hours = (duration % (3600 * 24)) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 987654
    result = convert_seconds(sample_duration)
    print(result)