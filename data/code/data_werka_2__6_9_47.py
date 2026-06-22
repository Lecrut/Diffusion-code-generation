def calculate_absolute_difference(weight1, weight2):
    difference = abs(weight1 - weight2)
    return difference

if __name__ == '__main__':
    initial_weight = 95.0
    subsequent_weight = 87.5
    absolute_diff = calculate_absolute_difference(initial_weight, subsequent_weight)
    print(absolute_diff)