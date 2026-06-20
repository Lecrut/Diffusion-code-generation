def compare_lengths(a, b):
    if a > b:
        return ("first", "greater")
    elif a < b:
        return ("second", "greater")
    else:
        return ("both", "equal")

if __name__ == '__main__':
    sample_a = 5.5
    sample_b = 3.2
    result = compare_lengths(sample_a, sample_b)
    print(result)