import sys
def calculate_count(input_data):
    total = 0
    for line in input_data:
        try:
            number = int(line.strip())
            total += 1
        except ValueError:
            pass
    return total
if __name__ == '__main__':
    sample_input = [
        "10",
        "25",
        "invalid",
        "30",
        "",
        "42.5"
    ]
    result = calculate_count(sample_input)
    print(result)