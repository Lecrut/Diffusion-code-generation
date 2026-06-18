def calculate_sum(input_data):
    total = 0
    for item in input_data:
        try:
            number = float(item)
            total += number
        except ValueError:
            break
    return total
if __name__ == '__main__':
    sample_input = "10 25 hello 3.5 42\n"
    input_lines = sample_input.split('\n')
    all_numbers = []
    for line in input_lines:
        if line.strip():
            all_numbers.extend(line.split())
    result = calculate_sum(all_numbers)
    print(result)