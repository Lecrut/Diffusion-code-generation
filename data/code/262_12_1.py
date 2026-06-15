if __name__ == '__main__':
    sample_input = [15, -3, 88, -102, 45]
    numbers = []
    input_str = " ".join(map(str, sample_input))
    try:
        if not input_str.strip():
            numbers = []
        else:
            input_list = [int(x) for x in input_str.split()]
            numbers = input_list
    except ValueError:
        numbers = []
    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"Input sequence: {sample_input}")
        print(f"The absolute smallest value is: {smallest}")
        print(f"The absolute largest value is: {largest}")
    else:
        print("No valid numbers were entered.")