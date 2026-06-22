def compare_two_simple_quantities_now_summary(a, b):
    summary = {
        'a': a,
        'b': b,
        'sum': a + b,
        'difference': abs(a - b),
        'product': a * b,
        'quotient': a / b if b != 0 else None
    }
    return summary

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    result = compare_two_simple_quantities_now_summary(sample_a, sample_b)
    print(f"Summary for {sample_a} and {sample_b}: {result}")