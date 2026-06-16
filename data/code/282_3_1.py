import sys
def calculate_sum(data):
    total = 0
    for item in data:
        try:
            total += int(item)
        except ValueError:
            pass
    return total
if __name__ == '__main__':
    sample_input = "10 25 hello 3.5 40\n"
    input_data = sample_input.split()
    result = calculate_sum(input_data)
    print(result)