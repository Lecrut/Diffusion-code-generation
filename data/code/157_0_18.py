def find_smallest(data):
    return min(data)

if __name__ == '__main__':
    sample_data = [42, 15, 89, 3, 77, 101]
    smallest_value = find_smallest(sample_data)
    print(smallest_value)