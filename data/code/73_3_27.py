def time_difference(t1: int, t2: int) -> int:
    return abs(t1 - t2)

if __name__ == '__main__':
    t1 = 1672531200
    t2 = 1672617600
    result = time_difference(t1, t2)
    print(result)