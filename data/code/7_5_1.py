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
    test_seconds1 = 7200
    result1 = convert_seconds(test_seconds1)
    print(f"Input: {test_seconds1}, Output: {result1}")
    test_seconds2 = 3661
    result2 = convert_seconds(test_seconds2)
    print(f"Input: {test_seconds2}, Output: {result2}")
    test_seconds3 = 125
    result3 = convert_seconds(test_seconds3)
    print(f"Input: {test_seconds3}, Output: {result3}")
    test_seconds4 = 0
    result4 = convert_seconds(test_seconds4)
    print(f"Input: {test_seconds4}, Output: {result4}")
    test_seconds5 = 3600
    result5 = convert_seconds(test_seconds5)
    print(f"Input: {test_seconds5}, Output: {result5}")