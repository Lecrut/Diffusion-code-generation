def perform_timsort(data):
    return sorted(data)

if __name__ == '__main__':
    sample_numbers = [42, 7, 19, 35, 11, 88]
    print("Original list:", sample_numbers)
    sorted_numbers = perform_timsort(sample_numbers)
    print("Sorted list:", sorted_numbers)