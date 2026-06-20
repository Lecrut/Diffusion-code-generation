def read_numbers():
    sample_input = "100 200 300 400 500"
    numbers = list(map(int, sample_input.split()))
    if not numbers:
        raise ValueError("No numbers provided")
    return numbers

if __name__ == '__main__':
    try:
        numbers = read_numbers()
        print(numbers[0], numbers[-1])
    except ValueError as e:
        print(e)