def swap_values(m, n):
    temp = m
    m = n
    n = temp
    return m, n

if __name__ == '__main__':
    value1, value2 = 7, 3
    value1, value2 = swap_values(value1, value2)
    print(f"Swapped values: value1={value1}, value2={value2}")