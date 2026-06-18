import math
def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)
def calculate_std_dev(data, mean):
    if len(data) < 2:
        return 0.0
    variance = sum([(x - mean) ** 2 for x in data]) / len(data)
    return math.sqrt(variance)
def compare_lists(list1, list2):
    mean1 = calculate_mean(list1)
    std_dev1 = calculate_std_dev(list1, mean1)
    mean2 = calculate_mean(list2)
    std_dev2 = calculate_std_dev(list2, mean2)
    print(f"List 1: {list1}")
    print(f"Mean of List 1: {mean1:.4f}")
    print(f"Standard Deviation of List 1: {std_dev1:.4f}")
    print("-" * 30)
    print(f"List 2: {list2}")
    print(f"Mean of List 2: {mean2:.4f}")
    print(f"Standard Deviation of List 2: {std_dev2:.4f}")
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    data2 = [10, 11, 12, 13, 14]
    compare_lists(data1, data2)