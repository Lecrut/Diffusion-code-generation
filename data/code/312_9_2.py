def find_largest_xor(nums):
    if not nums:
        return None
    result = nums[0]
    for i in range(1, len(nums)):
        result = result ^ nums[i]
    return result
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(find_largest_xor(list1))
    list2 = [5, 10, 15]
    print(find_largest_xor(list2))
    list3 = [7, 7, 7]
    print(find_largest_xor(list3))
    list4 = [10, 20, 30]
    print(find_largest_xor(list4))