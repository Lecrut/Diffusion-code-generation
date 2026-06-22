def convert_seconds(total_seconds):
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    sample_values = [0, 3661, 86400, 90061, 3600, 60, 1, 86401, 172800, 604800]
    for val in sample_values:
        print(convert_seconds(val))