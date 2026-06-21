def sort_mixed_numbers(lst):
    return sorted(lst, key=float)

if __name__ == '__main__':
    sample_values = [3.5, 2, 4.8, '1', 5]
    print(sort_mixed_numbers(sample_values))