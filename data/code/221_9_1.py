def custom_sort(a, b, c):
    if a > b:
        if a > c:
            if b > c:
                return a, c, b
            else:
                return a, b, c
        else:
            if b > c:
                return c, a, b
            else:
                return c, b, a
    else:
        if b > a:
            if b > c:
                return b, a, c
            else:
                return b, c, a
        else:
            if a > c:
                return c, a, b
            else:
                return c, b, a
if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    sorted_nums = custom_sort(num1, num2, num3)
    print(f"The sorted numbers are: {sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}")