import sys
def calculate_count(input_data):
    count = 0
    for line in input_data:
        try:
            number = int(line.strip())
            count += 1
        except ValueError:
            pass
    return count
if __name__ == '__main__':
    sample_input = [
        "10",
        "25",
        "error",
        "33",
        "",
        "42.5"
    ]
    total_count = calculate_count(sample_input)
    print(total_count)