import sys
def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    sample_inputs = [
        "10",
        "25",
        "error",
        "33",
        "42.5",
        "50"
    ]
    valid_integers = []
    for item in sample_inputs:
        try:
            number = int(item)
            valid_integers.append(number)
        except ValueError:
            continue
    mean_value = calculate_mean(valid_integers)
    print(mean_value)