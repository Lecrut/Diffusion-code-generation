def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b -= 1
    if a > b:
        return 0
    return (b - a) // 2 + 1

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    result = count_even_numbers(sample_a, sample_b)
    print(result)
    result_swapped = count_even_numbers(sample_b, sample_a)
    print(result_swapped)