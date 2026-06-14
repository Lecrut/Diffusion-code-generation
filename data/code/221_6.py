def order_three(a, b, c):
    nums = [a, b, c]
    nums.sort()
    return nums
if __name__ == '__main__':
    x = 5
    y = 2
    z = 8
    result = order_three(x, y, z)
    print(result)