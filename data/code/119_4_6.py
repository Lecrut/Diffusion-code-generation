def reverse_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return (b, a)

if __name__ == '__main__':
    print(reverse_two_numbers(3, 5))