def find_smallest(nums):
    if not nums:
        raise ValueError("List cannot be empty")
    smallest = nums[0]
    for num in nums[1:]:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    test_lists = [
        [3.14, 1.618, 2.718, 0.577, 9.81],
        [-10.5, 5.2, -3.1, 0.0, 1.1],
        [42.0],
        [7.777, 7.778, 7.7770]
    ]
    for test_list in test_lists:
        print(f"Smallest in {test_list}: {find_smallest(test_list)}")