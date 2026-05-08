import sys
def calculate_mean(inputs):
    valid_numbers = []
    for item in inputs:
        try:
            number = int(item.strip())
            valid_numbers.append(number)
        except ValueError:
            continue
    if not valid_numbers:
        return None
    return sum(valid_numbers) / len(valid_numbers)
if __name__ == '__main__':
    sample_input = [
        "10",
        "25",
        "hello",
        "30",
        "-5",
        "42.5",
        "100"
    ]
    mean_result = calculate_mean(sample_input)
    if mean_result is not None:
        print(mean_result)
    else:
        print("No valid integers found.")