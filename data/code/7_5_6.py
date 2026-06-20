def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        if remaining_seconds == 0:
            return f"{hours} hours"
        return f"{hours} hours {remaining_seconds} seconds"
    if total_seconds >= 60:
        minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60
        if remaining_seconds == 0:
            return f"{minutes} minutes"
        return f"{minutes} minutes {remaining_seconds} seconds"
    return f"{total_seconds} seconds"

if __name__ == '__main__':
    print(convert_seconds(7265))
    print(convert_seconds(150))
    print(convert_seconds(45))
    print(convert_seconds(3600))
    print(convert_seconds(12345))