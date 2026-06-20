MAX_VALUE = float('inf')

def get_max(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    print(get_max(5, 3))