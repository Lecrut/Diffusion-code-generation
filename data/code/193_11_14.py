def calculate_total(numbers: list[int]) -> int:
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(f"Total sum of {sample_list1}: {calculate_total(sample_list1)}")

    sample_list2 = [10, -5, 20, 0]
    total_of_sample2 = calculate_total(sample_list2)
    print(f"Total sum of {sample_list2}: {total_of_sample2}")

    empty_list = []
    print(f"Total sum of {empty_list}: {calculate_total(empty_list)}")

    single_element_list = [100]
    print(f"Total sum of {single_element_list}: {calculate_total(single_element_list)}")