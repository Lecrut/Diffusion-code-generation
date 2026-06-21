def sort_tuple(numbers):
    return tuple(sorted(numbers))

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.6)
    sorted_values = sort_tuple(sample_values)
    print(sorted_values)