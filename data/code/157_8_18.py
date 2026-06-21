def find_smallest(data):
    if not data:
        raise ValueError("List cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry"]
    print(find_smallest(sample_data))