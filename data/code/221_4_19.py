def order_numbers(a, b, c):
    nums = [a, b, c]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

if __name__ == '__main__':
    print(order_numbers(3.14, 2.71, 1.61))