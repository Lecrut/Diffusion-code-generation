def sort_three_numbers(numbers):
    numbers.sort()
if __name__ == '__main__':
    sample_list = [5, 2, 8]
    print(f"Original list: {sample_list}")
    sort_three_numbers(sample_list)
    print(f"Sorted list: {sample_list}")
    sample_list_2 = [100, 4, 50]
    print(f"\nOriginal list: {sample_list_2}")
    sort_three_numbers(sample_list_2)
    print(f"Sorted list: {sample_list_2}")
    sample_list_3 = [3.14, 1.618, 2.718]
    print(f"\nOriginal list: {sample_list_3}")
    sort_three_numbers(sample_list_3)
    print(f"Sorted list: {sample_list_3}")