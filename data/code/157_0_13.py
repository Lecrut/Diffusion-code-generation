def find_smallest(data):
    return min(data)

if __name__ == '__main__':
    sample_numbers = [42, 15, 89, 3, 77, 101]
    smallest_number = find_smallest(sample_numbers)
    print(smallest_number)