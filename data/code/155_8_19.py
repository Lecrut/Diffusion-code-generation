def sum_of_numbers(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

if __name__ == '__main__':
    sample_lists = {
        "sample_list1": [1, -2, 3, -4, 5],
        "sample_list2": [-10, 0, 5, -2.5],
        "sample_list3": [-1, -1, -1, -1],
        "sample_list4": [100],
        "sample_list5": []
    }

    for sample_name, sample_list in sample_lists.items():
        result = sum_of_numbers(sample_list)
        print(f"Result for {sample_name}: {result}")