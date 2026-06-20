def partition_and_sort(numbers):
    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    sorted_even = sorted(even)
    sorted_odd = sorted(odd)

    return sorted_even, sorted_odd

if __name__ == '__main__':
    sample_list_1 = [34, 7, 23, 90, 56, 89]
    result_1 = partition_and_sort(sample_list_1)
    print(f"Even List 1: {result_1[0]}")
    print(f"Odd List 1: {result_1[1]}")

    sample_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_2 = partition_and_sort(sample_list_2)
    print(f"Even List 2: {result_2[0]}")
    print(f"Odd List 2: {result_2[1]}")

    sample_list_3 = [11, 13, 15, 17]
    result_3 = partition_and_sort(sample_list_3)
    print(f"Even List 3: {result_3[0]}")
    print(f"Odd List 3: {result_3[1]}")

    sample_list_4 = []
    result_4 = partition_and_sort(sample_list_4)
    print(f"Even List 4: {result_4[0]}")
    print(f"Odd List 4: {result_4[1]}")