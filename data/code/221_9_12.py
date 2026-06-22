def custom_sort(a, b, c):
    if a > b:
        temp = a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    return a, b, c

if __name__ == '__main__':
    sample_values = [34, 12, 56]
    sorted_values = custom_sort(*sample_values)
    print(sorted_values)