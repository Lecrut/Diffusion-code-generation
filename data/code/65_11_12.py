def print_indexed_elements(data):
    for index, element in enumerate(data):
        print(f"Index {index}: {element}")

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Sample Data:")
    for item in sample_data:
        print(item)
    
    print("\nIndexed Elements:")
    print_indexed_elements(sample_data)