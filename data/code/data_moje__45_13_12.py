def find_minimum(values):
    min_val = values[0]
    for i in range(1, len(values)):
        if values[i] < min_val:
            min_val = values[i]
    return min_val

if __name__ == '__main__':
    sample_list = [45, 12, 78, -3, 56, 0, 23]
    result = find_minimum(sample_list)
    print(result)