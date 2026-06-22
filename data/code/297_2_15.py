def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    remaining_seconds = seconds % 60
    return f'{hours}h {minutes}m {remaining_seconds}s'
if __name__ == '__main__':
    print(convert_seconds_to_hms(3661))