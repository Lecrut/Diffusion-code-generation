def convert_duration(seconds):
    days = seconds // 86400
    remaining = seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    secs = remaining % 60
    return (days, hours, minutes, secs)

if __name__ == '__main__':
    print(convert_duration(0))
    print(convert_duration(86400))
    print(convert_duration(86401))
    print(convert_duration(3661))
    print(convert_duration(999999999))