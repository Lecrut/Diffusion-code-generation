def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
if __name__ == '__main__':
    sample_a = 10
    sample_b = 25
    sample_c = 15
    result = largest_of_three(sample_a, sample_b, sample_c)
    print(result)