def find_largest(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be integers or floats")
    return max(a, b, c)

if __name__ == '__main__':
    a = 10
    b = 25
    c = 15
    print(f"The largest number is: {find_largest(a, b, c)}")