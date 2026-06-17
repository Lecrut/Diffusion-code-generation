if __name__ == '__main__':
    sample_input = [15, -3, 42, 8, -100, 77]
    numbers = []
    is_valid = True
    for item in sample_input:
        try:
            numbers.append(int(item))
        except ValueError:
            is_valid = False
            break
    if is_valid and numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"Input sequence: {sample_input}")
        print(f"Stored integers: {numbers}")
        print(f"Smallest value: {smallest}")
        print(f"Largest value: {largest}")
    else:
        print("Error: Could not process the input. Ensure all elements are valid integers.")