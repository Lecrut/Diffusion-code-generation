import random
def sort_numbers(numbers: list) -> list:
    return sorted(numbers)
if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_data)
    result_list = sort_numbers(sample_data.copy())
    print("Sorted list:", result_list)