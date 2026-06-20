def sort_mixed_list(mixed_list):
    return sorted(mixed_list, key=str)

if __name__ == '__main__':
    sample_values = ['apple', 3, 'banana', 2, 'cherry']
    print(sort_mixed_list(sample_values))