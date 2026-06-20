def swap_numbers(m, n):
    temp = m
    m = n
    n = temp
    return m, n

if __name__ == '__main__':
    i, j = 7, 14
    i, j = swap_numbers(i, j)
    print(f"Swapped values: i={i}, j={j}")