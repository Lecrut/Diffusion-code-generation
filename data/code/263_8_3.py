def count_greater_pairs(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] > nums[j]:
                count += 1
    return count
if __name__ == '__main__':
    list1 = [1, 2, 3]
    print(count_greater_pairs(list1))
    list2 = [3, 1, 2]
    print(count_greater_pairs(list2))
    list3 = [5, 4, 3, 2, 1]
    print(count_greater_pairs(list3))
    list4 = [1, 1, 2, 2]
    print(count_greater_pairs(list4))