def find_the_middle_value_among_three_summary(a, b, c):
    values = {'a': a, 'b': b, 'c': c}
    sorted_values = sorted(values.values())
    return sorted_values[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_summary(3, 1, 2))