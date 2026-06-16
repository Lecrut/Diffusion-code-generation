if __name__ == '__main__':
    input_string = "10,25,33,invalid,42"
    numbers = []
    try:
        for item in input_string.split(','):
            numbers.append(int(item.strip()))
        total_sum = sum(numbers)
        print(f"Total sum: {total_sum}")
    except ValueError:
        print("Error: Input contains non-numeric values.")