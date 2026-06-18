import sys
def calculate_sum(input_data):
    total = 0
    for line in input_data:
        try:
            number = float(line.strip())
            total += number
        except ValueError:
            break
    return total
if __name__ == '__main__':
    sample_input = [
        "10",
        "25.5",
        "30",
        "error",
        "42"
    ]
    result = calculate_sum(sample_input)
    print(result)