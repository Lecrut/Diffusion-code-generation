def calculate_sum(input_data):
    total = 0
    for value in input_data:
        try:
            number = int(value.strip())
            total += number
        except ValueError:
            continue
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