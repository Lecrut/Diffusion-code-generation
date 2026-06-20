def swap_values(x, y):
    temp = x
    x = y
    y = temp
    return x, y

if __name__ == '__main__':
    value1, value2 = 7, 3
    value1, value2 = swap_values(value1, value2)
    print(f"Swapped values: value1={value1}, value2={value2}")