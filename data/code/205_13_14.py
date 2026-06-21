def sort_tuple_ascending(float_tuple):
    return tuple(sorted(float_tuple))

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    sorted_values = sort_tuple_ascending(sample_values)
    print(sorted_values)