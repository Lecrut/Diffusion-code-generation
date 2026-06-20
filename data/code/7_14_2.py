def convert_seconds(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    test_values = [0, 60, 3600, 86400, 93784, 31536000]
    for val in test_values:
        print(val, "->", convert_seconds(val))