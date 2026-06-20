def validate_data(data):
    for item in data:
        if not isinstance(item, (str, int)):
            raise ValueError("All elements must be either strings or integers")

def sort_mixed_data(data):
    return sorted(data, key=str)

if __name__ == '__main__':
    sample_data = [5, "apple", 3, "banana", "cherry", 2]
    validate_data(sample_data)
    sorted_data = sort_mixed_data(sample_data)
    print(sorted_data)