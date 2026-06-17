if __name__ == '__main__':
    sample_input = [15, -3, 42, 8, 99, -10]
    numbers = []
    all_valid = True
    for item in sample_input:
        try:
            numbers.append(int(item))
        except ValueError:
            all_valid = False
            break
    if not all_valid:
        print("Error: Input contained non-integer values.")
    else:
        if not numbers:
            print("The list is empty.")
        else:
            smallest = min(numbers)
            largest = max(numbers)
            print(f"Input sequence: {sample_input}")
            print(f"Stored integers: {numbers}")
            print(f"Absolute smallest value: {smallest}")
            print(f"Absolute largest value: {largest}")