def validate_data(data):
    if not isinstance(data, list) or len(data) != 3:
        raise ValueError("Input must be a list of exactly three integers")

def find_median(data):
    validate_data(data)
    sorted_data = sorted(data)
    n = len(sorted_data)
    return sorted_data[n // 2]

if __name__ == '__main__':
    sample_list1 = [3, 1, 4]
    print(f"Median of {sample_list1}: {find_median(sample_list1)}")

    sample_list2 = [10, 5, 15]
    print(f"Median of {sample_list2}: {find_median(sample_list2)}")

    sample_list3 = [7, 2, 4]
    print(f"Median of {sample_list3}: {find_median(sample_list3)}")