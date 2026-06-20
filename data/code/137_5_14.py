MAX_VALUE = 2**31 - 1

def get_max(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    print(get_max(5, 3))
    print(get_max(-1, -5))
    print(get_max(MAX_VALUE, MAX_VALUE - 1))