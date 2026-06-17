import math
def calculate_median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_data1 = [5, 2, 8, 1, 9]
    print(f"Median of {sample_data1}: {calculate_median(sample_data1)}")
    sample_data2 = [1, 3, 5, 7, 9]
    print(f"Median of {sample_data2}: {calculate_median(sample_data2)}")
    sample_data3 = [4, 1, 8, 3, 6, 2, 5]
    print(f"Median of {sample_data3}: {calculate_median(sample_data3)}")
    sample_data4 = [10, 20, 30, 40]
    print(f"Median of {sample_data4}: {calculate_median(sample_data4)}")