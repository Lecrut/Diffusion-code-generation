def is_before(timestamp1: float, timestamp2: float) -> bool:
    return timestamp1 < timestamp2

if __name__ == '__main__':
    result = is_before(1672531200.0, 1672617600.0)
    print(result)