def partition_and_sort(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return sorted(even_numbers), sorted(odd_numbers)

if __name__ == '__main__':
    sample_list_1 = [3, 5, 8, 10, 2, 9]
    result_1 = partition_and_sort(sample_list_1)
    print(f"Original List 1: {sample_list_1}")
    print(f"Even Sorted List 1: {result_1[0]}")
    print(f"Odd Sorted List 1: {result_1[1]}")

    sample_list_2 = [4, 1, 7, 6, 3, 8]
    result_2 = partition_and_sort(sample_list_2)
    print(f"\nOriginal List 2: {sample_list_2}")
    print(f"Even Sorted List 2: {result_2[0]}")
    print(f"Odd Sorted List 2: {result_2[1]}")

    sample_list_3 = [0, 2, 4, 6, 8]
    result_3 = partition_and_sort(sample_list_3)
    print(f"\nOriginal List 3: {sample_list_3}")
    print(f"Even Sorted List 3: {result_3[0]}")
    print(f"Odd Sorted List 3: {result_3[1]}")

    sample_list_4 = [1, 3, 5, 7]
    result_4 = partition_and_sort(sample_list_4)
    print(f"\nOriginal List 4: {sample_list_4}")
    print(f"Even Sorted List 4: {result_4[0]}")
    print(f"Odd Sorted List 4: {result_4[1]}")

    sample_list_5 = []
    result_5 = partition_and_sort(sample_list_5)
    print(f"\nOriginal List 5: {sample_list_5}")
    print(f"Even Sorted List 5: {result_5[0]}")
    print(f"Odd Sorted List 5: {result_5[1]}")