def time_difference_in_hours(timestamp1, timestamp2):
    return abs((timestamp2 - timestamp1) / 3600)

if __name__ == '__main__':
    print(time_difference_in_hours(1672531200.0, 1672617600.0))