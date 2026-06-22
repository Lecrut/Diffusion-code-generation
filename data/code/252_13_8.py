def validate_samples(sample1, sample2):
    if not isinstance(sample1, (int, float)) or not isinstance(sample2, (int, float)):
        raise ValueError("Both samples must be numbers")

def compare_two_simple_quantities_now_rank_samples(sample1, sample2):
    validate_samples(sample1, sample2)
    return sorted([sample1, sample2])

if __name__ == '__main__':
    num1 = 10.5
    num2 = 5.2
    result = compare_two_simple_quantities_now_rank_samples(num1, num2)
    print(result)

    num3 = 3
    num4 = 7
    result2 = compare_two_simple_quantities_now_rank_samples(num3, num4)
    print(result2)

    num5 = -1.0
    num6 = -5.0
    result3 = compare_two_simple_quantities_now_rank_samples(num5, num6)
    print(result3)