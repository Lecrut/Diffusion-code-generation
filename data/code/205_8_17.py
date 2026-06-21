def sort_mixed_numbers(mixed_list):
    return sorted(mixed_list, key=lambda x: float(x))

if __name__ == '__main__':
    sample_values = [3, 2.5, '1', 4, '0.9']
    print(sort_mixed_numbers(sample_values))