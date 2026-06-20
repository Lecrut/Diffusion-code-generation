def stable_sort_mixed(data):
    return sorted(data, key=lambda x: str(x))

if __name__ == '__main__':
    sample_data = [3, "apple", 2, "banana", "1", 4]
    print(stable_sort_mixed(sample_data))