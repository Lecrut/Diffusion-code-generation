def find_median(nums):
    nums_len = len(nums)
    if nums_len % 2 == 1:
        return sorted(nums)[nums_len // 2]
    else:
        mid1, mid2 = sorted(nums)[nums_len // 2 - 1], sorted(nums)[nums_len // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(find_median(sample_data))