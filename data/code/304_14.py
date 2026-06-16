precedes = lambda d1, d2: d1 < d2
if __name__ == '__main__':
    print(precedes("2023-01-01", "2023-01-02"))
    print(precedes("2023-01-02", "2023-01-01"))