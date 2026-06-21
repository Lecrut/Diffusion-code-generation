def min_float_value(lst):
    return min(float(x) for x in lst)

if __name__ == '__main__':
    sample_values = [3, 5.5, '2', 4]
    print(min_float_value(sample_values))