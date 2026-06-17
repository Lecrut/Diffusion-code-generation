def demonstrate_printing():
    sample_list = [10, 20, 30, 40, 50]
    print("--- Using for loop ---")
    for item in sample_list:
        print(item)
    print("\n--- Using while loop ---")
    i = 0
    while i < len(sample_list):
        print(sample_list[i])
        i += 1
    print("\n--- Using list comprehension ---")
    result = [item for item in sample_list]
    print(result)
if __name__ == '__main__':
    demonstrate_printing()