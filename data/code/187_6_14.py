def find_largest_number(data):
    if not data:
        raise ValueError("The list cannot be empty.")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Largest number in sample list:", find_largest_number(sample_list))
    
    large_sample = [100, 50, 200, 10, 300, 150]
    print("Largest number in large sample list:", find_largest_number(large_sample))