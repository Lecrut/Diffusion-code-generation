import math
def find_median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
def filter_by_median(data):
    if not data:
        return []
    median_value = find_median(data)
    result = [x for x in data if x > median_value]
    return result
if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    print(f"Sample List 1: {sample_list1}")
    print(f"Result 1: {filter_by_median(sample_list1)}")
    sample_list2 = [1, 2, 3, 4, 5, 6]
    print(f"Sample List 2: {sample_list2}")
    print(f"Result 2: {filter_by_median(sample_list2)}")
    sample_list3 = [10, 20, 30, 40, 50, 60]
    print(f"Sample List 3: {sample_list3}")
    print(f"Result 3: {filter_by_median(sample_list3)}")
    sample_list4 = [1, 2, 8, 9, 10]
    print(f"Sample List 4: {sample_list4}")
    print(f"Result 4: {filter_by_median(sample_list4)}")
    sample_list5 = [1, 1, 2, 2, 3]
    print(f"Sample List 5: {sample_list5}")
    print(f"Result 5: {filter_by_median(sample_list5)}")