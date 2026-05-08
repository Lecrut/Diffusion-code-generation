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
    sample_list_1 = [5.5, -2, 10, -1.5, 0]
    sample_list_2 = []
    sample_list_3 = [-100, -50, 0, 10, 20.5]
    sample_list_4 = [-3, -1, -5, -10]
    sample_list_5 = [1.1, 2.2, 3.3]
    sample_list_6 = []
    print(f"Sample 1: {sort_mixed_numbers(sample_list_1)}")
    print(f"Sample 2: {sort_mixed_numbers(sample_list_2)}")
    print(f"Sample 3: {sort_mixed_numbers(sample_list_3)}")
    print(f"Sample 4: {sort_mixed_numbers(sample_list_4)}")
    print(f"Sample 5: {sort_mixed_numbers(sample_list_5)}")
    print(f"Sample 6: {sort_mixed_numbers(sample_list_6)}")