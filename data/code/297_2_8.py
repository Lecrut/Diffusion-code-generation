def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    remaining_seconds = seconds % 60
    return f'{hours:02}:{minutes:02}:{remaining_seconds:02}'
if __name__ == '__main__':
    print(seconds_to_hms(3661))