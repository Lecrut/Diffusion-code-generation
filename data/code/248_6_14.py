def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return a + b

if __name__ == '__main__':
    result1 = add(5, 3)
    print(f"The sum of 5 and 3 is: {result1}")
    result2 = add(-2, 7)
    print(f"The sum of -2 and 7 is: {result2}")