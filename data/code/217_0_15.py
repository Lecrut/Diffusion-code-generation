def compare_integers(a, b):
    if a > b:
        return "greater than"
    elif a < b:
        return "less than"
    else:
        return "equal to"

if __name__ == '__main__':
    sample_a = 8
    sample_b = 12
    result = compare_integers(sample_a, sample_b)
    print(result)