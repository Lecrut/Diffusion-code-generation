import math
def sort_mixed_numbers(data):
    if not data:
        return []
    try:
        sorted_data = sorted(data)
        return sorted_data
    except TypeError:
        return []
if __name__ == '__main__':
    sample_list_1 = [5.5, -1.2, 0, 3.14, -10]
    sample_list_2 = []
    sample_list_3 = [-5, -1, 0, 100, 50.5]
    sample_list_4 = []
    sample_list_5 = [1, 2, 3, 4]
    sample_list_6 = [-10, -5, -1, -2]
    print("Sample 1:", sort_mixed_numbers(sample_list_1))
    print("Sample 2:", sort_mixed_numbers(sample_list_2))
    print("Sample 3:", sort_mixed_numbers(sample_list_3))
    print("Sample 4:", sort_mixed_numbers(sample_list_4))
    print("Sample 5:", sort_mixed_numbers(sample_list_5))
    print("Sample 6:", sort_mixed_numbers(sample_list_6))