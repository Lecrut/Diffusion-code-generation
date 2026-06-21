def sort_tuple(items):
    return tuple(sorted(items))

if __name__ == '__main__':
    sample_data = (3.14, 1, 5.0, 2, 9.9)
    sorted_data = sort_tuple(sample_data)
    print("Sorted data:", sorted_data)