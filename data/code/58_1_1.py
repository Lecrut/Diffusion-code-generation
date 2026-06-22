def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    count = 0
    start = a if a % 2 == 0 else a + 1
    for num in range(start, b + 1, 2):
        count += 1
    return count

if __name__ == '__main__':
    result = count_even_numbers(3, 9)
    print(result)