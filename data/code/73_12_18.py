def time_difference(timestamp1, timestamp2):
    return abs((timestamp2 - timestamp1) / 3600)
if __name__ == '__main__':
    print(time_difference(1633075200.0, 1633161600.0))