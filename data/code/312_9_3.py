def find_largest_xor(nums):
    if not nums:
        return None
    result = nums[0]
    for i in range(1, len(nums)):
        result = result ^ nums[i]
    return result
if __name__ == '__main__':
    list1 = [3, 10, 5, 25, 2, 8]
    print(find_largest_xor(list1))
    list2 = [1, 2, 3, 4, 5]
    print(find_largest_xor(list2))
    list3 = [10, 20, 30]
    print(find_largest_xor(list3))