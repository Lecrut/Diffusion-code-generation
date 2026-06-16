import sys
def calculate_sum(input_data):
    total = 0
    for item in input_data:
        try:
            total += int(item)
        except ValueError:
            pass
    return total
if __name__ == '__main__':
    sample_input = [10, 5.5, "20", "invalid", 3]
    result = calculate_sum(sample_input)
    print(result)