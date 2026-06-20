def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds / 3600
        return f"{hours} hours"
    elif total_seconds >= 60:
        minutes = total_seconds / 60
        return f"{minutes} minutes"
    else:
        return f"{total_seconds} seconds"

if __name__ == '__main__':
    print(convert_seconds(7265))
    print(convert_seconds(150))
    print(convert_seconds(45))