import sys
def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    sample_input = [
        "10",
        "25",
        "error",
        "30",
        "42.5",
        "5"
    ]
    valid_integers = []
    for item in sample_input:
        try:
            number = int(item)
            valid_integers.append(number)
        except ValueError:
            pass
    mean_value = calculate_mean(valid_integers)
    print(mean_value)