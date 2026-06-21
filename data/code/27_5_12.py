def is_valid_triangle(a, b, c):
    nums = [a, b, c]
    for x in nums:
        if not (x > 0):
            return False
    nums.sort()
    return nums[0] + nums[1] > nums[2]

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(0, 4, 5))
    print(is_valid_triangle(10, 1, 1))
    print(is_valid_triangle(7, 8, 9))
    print(is_valid_triangle(1, 1, 2))