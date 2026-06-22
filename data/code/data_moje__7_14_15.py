def convert_duration(seconds):
    days = seconds // 86400
    remainder = seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    remaining_seconds = remainder % 60
    return (days, hours, minutes, remaining_seconds)

if __name__ == '__main__':
    result = convert_duration(1234567)
    print(result)