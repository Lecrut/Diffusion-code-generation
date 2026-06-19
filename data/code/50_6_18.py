def non_negative_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    sample_values = [10, 5, 8, 2, 15]
    for i in range(1, len(sample_values)):
        print(non_negative_difference(sample_values[i], sample_values[i-1]))