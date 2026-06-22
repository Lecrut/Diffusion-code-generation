MAX_VALUE = float('inf')

def find_largest(a, b, c):
    largest = max(a, b, c)
    return largest

if __name__ == '__main__':
    a = 10
    b = 25
    c = 15
    result = find_largest(a, b, c)
    print(f"The largest value among {a}, {b}, and {c} is: {result}")