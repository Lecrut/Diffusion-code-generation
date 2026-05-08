import random
def sort_mixed_numbers(data):
    if not data:
        return []
    try:
        sorted_data = sorted(data)
        return sorted_data
    except TypeError:
        return []
if __name__ == '__main__':
    sample_list = [5.5, -2, 10, -1.5, 0, 3.14, -8, 7]
    sorted_result = sort_mixed_numbers(sample_list)
    print(sorted_result)