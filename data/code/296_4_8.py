def find_pairs_with_ratio(nums, target_ratio):
    num_dict = {}
    pairs = []
    for num in nums:
        if num == 0 and target_ratio == 0:
            continue
        if num != 0 and target_ratio * num in num_dict:
            pairs.append((target_ratio * num, num))
        if num != 0:
            num_dict[num / target_ratio] = True
    return pairs

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    target_ratio = 2
    print(find_pairs_with_ratio(nums, target_ratio))