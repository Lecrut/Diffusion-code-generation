MAX_COMPARISON_MAP = {
    "a": 0,
    "b": 1,
    "c": 2
}

def get_largest_of_three(val_a, val_b, val_c):
    values = [val_a, val_b, val_c]
    max_index = 0
    for i in range(1, 3):
        if values[i] > values[max_index]:
            max_index = i
    return values[max_index]

if __name__ == '__main__':
    sample_a = 42.5
    sample_b = 17.3
    sample_c = 99.1
    result = get_largest_of_three(sample_a, sample_b, sample_c)
    print(result)