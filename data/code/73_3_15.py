def time_difference(t1, t2):
    return abs(t1 - t2)

if __name__ == '__main__':
    t1 = 1609459200
    t2 = 1609462800
    result = time_difference(t1, t2)
    print(result)