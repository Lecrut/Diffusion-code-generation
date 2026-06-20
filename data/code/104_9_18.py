def is_time_before(timestamp1: float, timestamp2: float) -> bool:
    return timestamp1 < timestamp2

if __name__ == '__main__':
    print(is_time_before(1633072800.0, 1633076400.0))