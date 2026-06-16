def find_largest_xor(nums):
    if not nums:
        return None
    largest = nums[0]
    for i in range(1, len(nums)):
        largest = largest ^ nums[i]
    return largest
if __name__ == '__main__':
    list1 = [3, 10, 5, 25, 2, 8]
    print(find_largest_xor(list1))
    list2 = [12, 34, 67, 89, 1]
    print(find_largest_xor(list2))
    list3 = [7, 7, 7, 7]
    print(find_largest_xor(list3))
    list4 = [5]
    print(find_largest_xor(list4))