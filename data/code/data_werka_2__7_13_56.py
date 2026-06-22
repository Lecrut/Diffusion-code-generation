def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    total_seconds = convert_to_seconds(2, 45, 30)
    print(total_seconds)