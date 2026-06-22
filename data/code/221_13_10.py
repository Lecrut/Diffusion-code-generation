if __name__ == '__main__':
    a, b, c = 10, 5, 20
    numbers = [a, b, c]
    if not all(isinstance(n, int) for n in numbers):
        raise ValueError("All values must be integers")
    sorted_sequence = sorted(numbers, key=lambda x: x)
    print(sorted_sequence)