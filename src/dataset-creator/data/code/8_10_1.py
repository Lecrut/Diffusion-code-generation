import math
def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)
def calculate_std_dev(data, mean):
    if len(data) < 2:
        return 0.0
    variance = sum([(x - mean) ** 2 for x in data]) / (len(data) - 1)
    return math.sqrt(variance)
def compare_lists(list1, list2):
    mean1 = calculate_mean(list1)
    std_dev1 = calculate_std_dev(list1, mean1)
    mean2 = calculate_mean(list2)
    std_dev2 = calculate_std_dev(list2, mean2)
    print("--- List 1 Statistics ---")
    print(f"Mean: {mean1:.4f}")
    print(f"Standard Deviation: {std_dev1:.4f}")
    print("\n--- List 2 Statistics ---")
    print(f"Mean: {mean2:.4f}")
    print(f"Standard Deviation: {std_dev2:.4f}")
    if mean1 == mean2 and std_dev1 == std_dev2:
        print("\nComparison Result: The means and standard deviations are identical.")
    else:
        print("\nComparison Result: The statistics for the two lists are different.")
if __name__ == '__main__':
    list_a = [10, 12, 23, 23, 16, 23, 21, 16]
    list_b = [15, 17, 20, 22, 18, 21, 19, 20]
    compare_lists(list_a, list_b)