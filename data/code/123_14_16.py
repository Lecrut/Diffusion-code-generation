def calculate_sum(input_data):
    total = 0
    for item in input_data:
        try:
            number = int(item.strip())
            total += number
        except ValueError:
            print(f"Error: Invalid input '{item.strip()}' found. Skipping.")
    return total

if __name__ == '__main__':
    sample_input = [
        "10",
        "25",
        "hello",
        "30",
        "-5"
    ]
    result = calculate_sum(sample_input)
    print(result)