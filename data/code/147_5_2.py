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
    sample_list = [10.5, -5, 3.14, 0, -100, 22, -1.5, 7]
    sorted_result = sort_mixed_numbers(sample_list)
    print(sorted_result)