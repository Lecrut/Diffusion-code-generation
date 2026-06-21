def sort_tuple(tup):
    return tuple(sorted(tup))

if __name__ == '__main__':
    sample_data = (3.14, 1, 5.0, 2, 9.9)
    sorted_data = sort_tuple(sample_data)
    print("Sorted tuple:", sorted_data)