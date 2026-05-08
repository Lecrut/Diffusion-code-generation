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
        "5",
        "30.5",
        "12"
    ]
    valid_integers = []
    for line in sample_inputs:
        try:
            number = int(line)
            valid_integers.append(number)
        except ValueError:
            pass
    mean_value = calculate_mean(valid_integers)
    print(mean_value)