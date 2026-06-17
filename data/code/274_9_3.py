def demonstrate_printing():
    sample_list = [10, 20, 30, 40, 50]
    print("--- Method 1: For Loop ---")
    for item in sample_list:
        print(item)
    print("\n--- Method 2: While Loop ---")
    i = 0
    while i < len(sample_list):
        print(sample_list[i])
        i += 1
    print("\n--- Method 3: List Comprehension ---")
    result = [item for item in sample_list]
    print(result)
if __name__ == '__main__':
    demonstrate_printing()