def time_difference(timestamp1: float, timestamp2: float) -> float:
    return abs((timestamp2 - timestamp1) / 3600)

if __name__ == '__main__':
    print(time_difference(1672531200.0, 1672534800.0))