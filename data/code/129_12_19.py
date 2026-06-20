def partition_and_sort(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    
    even_numbers.sort()
    odd_numbers.sort()
    
    return even_numbers, odd_numbers

if __name__ == '__main__':
    sample_list_1 = [34, 7, 23, 89, 56, 2, 11, 45]
    result_1 = partition_and_sort(sample_list_1)
    print(f"Even Numbers: {result_1[0]}")
    print(f"Odd Numbers: {result_1[1]}\n")

    sample_list_2 = [12, 3, 78, 54, 9, 65]
    result_2 = partition_and_sort(sample_list_2)
    print(f"Even Numbers: {result_2[0]}")
    print(f"Odd Numbers: {result_2[1]}\n")

    sample_list_3 = [8, 6, 4, 2, 0]
    result_3 = partition_and_sort(sample_list_3)
    print(f"Even Numbers: {result_3[0]}")
    print(f"Odd Numbers: {result_3[1]}\n")

    sample_list_4 = [7, 5, 3, 1]
    result_4 = partition_and_sort(sample_list_4)
    print(f"Even Numbers: {result_4[0]}")
    print(f"Odd Numbers: {result_4[1]}\n")