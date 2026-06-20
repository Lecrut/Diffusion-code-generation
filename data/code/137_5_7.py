def get_max(a, b):
    return a if a > b else b

if __name__ == '__main__':
    print(get_max(5, 3))
    print(get_max(-1, -5))
    print(get_max(0, 0))