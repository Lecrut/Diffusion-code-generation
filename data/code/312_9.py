def find_largest_xor(nums):
    if not nums:
        return None
    largest = nums[0]
    for i in range(1, len(nums)):
        largest = largest ^ nums[i]
    return largest
if __name__ == '__main__':
    list1 = [3, 5, 8, 2]
    print(find_largest_xor(list1))
    list2 = [10, 5, 2, 7, 8]
    print(find_largest_xor(list2))
    list3 = [42]
    print(find_largest_xor(list3))
    list4 = [1, 2, 3, 4]
    print(find_largest_xor(list4))