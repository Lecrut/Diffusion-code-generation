MAX_VALUE = float('-inf')

def find_maximum(a, b, c):
    global MAX_VALUE
    if a > MAX_VALUE:
        MAX_VALUE = a
    if b > MAX_VALUE:
        MAX_VALUE = b
    if c > MAX_VALUE:
        MAX_VALUE = c
    return MAX_VALUE

if __name__ == '__main__':
    result = find_maximum(10, 20, 30)
    print(f"Largest number: {result}")