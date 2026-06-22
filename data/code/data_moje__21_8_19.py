def find_largest(value_first, value_second, value_third):
    candidates = [value_first, value_second, value_third]
    current_max = candidates[ZERO_INDEX]
    for index in range(ONE_INDEX, LENGTH_THREE):
        if candidates[index] > current_max:
            current_max = candidates[index]
    return current_max

ZERO_INDEX = 0
ONE_INDEX = 1
LENGTH_THREE = 3

if __name__ == '__main__':
    first_sample = 42.0
    second_sample = 15.5
    third_sample = 88.9
    output = find_largest(first_sample, second_sample, third_sample)
    print(output)