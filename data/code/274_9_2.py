def main():
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("--- Using for loop ---")
    for item in sample_list:
        print(item)
    print("\n--- Using while loop ---")
    i = 0
    while i < len(sample_list):
        print(sample_list[i])
        i += 1
    print("\n--- Using list comprehension ---")
    list_comprehension_result = [item for item in sample_list]
    for item in list_comprehension_result:
        print(item)
if __name__ == '__main__':
    main()