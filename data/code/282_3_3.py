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
    sample_input = "10 5 hello 22.5 -3\n"
    input_data = sample_input.split()
    final_sum = calculate_sum(input_data)
    print(final_sum)