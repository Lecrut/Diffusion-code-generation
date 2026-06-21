def sort_tuple(numbers):
    return tuple(sorted(numbers))

if __name__ == '__main__':
    sample_data = (3.14, 1, 5.5, 2, 8.9)
    sorted_data = sort_tuple(sample_data)
    print("Sorted tuple:", sorted_data)