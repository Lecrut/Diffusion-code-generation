def reverse_numbers(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")
    return (b, a)

if __name__ == '__main__':
    print(reverse_numbers(3, 5))