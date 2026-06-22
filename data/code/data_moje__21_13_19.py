def get_max_of_three(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 25.3
    sample_c = 18.7
    print(get_max_of_three(sample_a, sample_b, sample_c))