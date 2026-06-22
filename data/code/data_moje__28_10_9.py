def sort_two_integers(a, b):
    if a <= b:
        return a, b
    return b, a

if __name__ == '__main__':
    sample_a = 42
    sample_b = 17
    result = sort_two_integers(sample_a, sample_b)
    print(result)