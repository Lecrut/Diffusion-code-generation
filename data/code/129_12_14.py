def partition_and_sort_by_parity(int_list):
    even_numbers = [num for num in int_list if num % 2 == 0]
    odd_numbers = [num for num in int_list if num % 2 != 0]
    return sorted(even_numbers), sorted(odd_numbers)

if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even_list_1, odd_list_1 = partition_and_sort_by_parity(sample_list_1)
    print(f"Even Numbers: {even_list_1}")
    print(f"Odd Numbers: {odd_list_1}")

    sample_list_2 = [10, 23, 45, 68, 79, 81, 92]
    even_list_2, odd_list_2 = partition_and_sort_by_parity(sample_list_2)
    print(f"Even Numbers: {even_list_2}")
    print(f"Odd Numbers: {odd_list_2}")

    sample_list_3 = [0, -1, -2, -3, 4, 5]
    even_list_3, odd_list_3 = partition_and_sort_by_parity(sample_list_3)
    print(f"Even Numbers: {even_list_3}")
    print(f"Odd Numbers: {odd_list_3}")

    sample_list_4 = []
    even_list_4, odd_list_4 = partition_and_sort_by_parity(sample_list_4)
    print(f"Even Numbers: {even_list_4}")
    print(f"Odd Numbers: {odd_list_4}")