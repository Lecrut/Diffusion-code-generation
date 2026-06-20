def calculate_time_difference(timestamp1, timestamp2):
    time_difference = abs(timestamp2 - timestamp1)
    return time_difference

if __name__ == '__main__':
    result = calculate_time_difference(1635702400, 1635875200)
    print(result)