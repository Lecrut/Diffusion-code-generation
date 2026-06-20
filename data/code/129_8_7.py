def sort_mixed_list(mixed_list):
    return sorted(mixed_list, key=lambda x: str(x))

if __name__ == '__main__':
    sample_values = [3, "apple", 2, "banana", "1", 4]
    print(sort_mixed_list(sample_values))