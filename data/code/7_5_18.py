def convert_seconds(seconds):
    if seconds >= 3600:
        hours = seconds / 3600
        return f"{hours:.2f} hours"
    elif seconds >= 60:
        minutes = seconds / 60
        return f"{minutes:.2f} minutes"
    else:
        return f"{seconds} seconds"

if __name__ == '__main__':
    print(convert_seconds(3661))
    print(convert_seconds(125))
    print(convert_seconds(45))
    print(convert_seconds(0))
    print(convert_seconds(86400))