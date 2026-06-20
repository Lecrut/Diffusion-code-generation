def reverse_two_numbers(a, b):
    if not all(isinstance(i, int) for i in [a, b]):
        raise ValueError("Both inputs must be integers.")
    return (b, a)

if __name__ == '__main__':
    try:
        print(reverse_two_numbers(10, 20))
    except ValueError as e:
        print(e)