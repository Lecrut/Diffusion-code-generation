def count_even_integers(a, b):
    start = min(a, b)
    end = max(a, b)

    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1

    if first_even > last_even:
        return 0

    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    sample_a = 3
    sample_b = 15
    result = count_even_integers(sample_a, sample_b)
    print(result)