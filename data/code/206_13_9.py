def min_of_floats(lst):
    return min(filter(lambda x: isinstance(x, (int, float)), lst))

if __name__ == '__main__':
    sample_values = [3.5, 2, 'a', None, 4.5]
    print(min_of_floats(sample_values))