def custom_sort(a, b, c):
    if a > b:
        temp = a
        a = b
        b = temp
    else:
        temp = a
        a = b
        b = temp
    if a > c:
        temp = a
        a = c
        c = temp
    else:
        temp = a
        a = c
        c = temp
    if a > b:
        temp = a
        a = b
        b = temp
    return a, b, c
if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    sorted_num1, sorted_num2, sorted_num3 = custom_sort(num1, num2, num3)
    print(f"The sorted numbers are: {sorted_num1}, {sorted_num2}, {sorted_num3}")