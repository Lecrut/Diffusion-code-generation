def sort_mixed_list(mixed_list):
    return sorted(mixed_list, key=lambda x: str(x))

if __name__ == '__main__':
    sample_values = [3, "apple", 1, "banana", 2]
    print(sort_mixed_list(sample_values))