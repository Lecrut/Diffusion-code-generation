def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    count = 0
    for num in range(a, b + 1):
        if num % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    sample_a = 3
    sample_b = 10
    result = count_even_numbers(sample_a, sample_b)
    print(result)