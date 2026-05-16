def convert_seconds(seconds):
    if seconds > 3600:
        hours = seconds // 3600
        return hours
    elif seconds > 60:
        minutes = seconds // 60
        return minutes
    else:
        return seconds
if __name__ == '__main__':
    test_cases = [
        10,
        60,
        61,
        3599,
        3600,
        3601,
        7200,
        86400
    ]
    for seconds in test_cases:
        result = convert_seconds(seconds)
        print(f"Input: {seconds}, Output: {result}")