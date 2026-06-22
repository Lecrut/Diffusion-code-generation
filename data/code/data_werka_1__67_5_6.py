def add_numbers(a, b):
    try:
        result = float(a) + float(b)
        return result
    except ValueError:
        return "Error: Both inputs must be numbers."

if __name__ == '__main__':
    sample1_a = 7.5
    sample1_b = '2.3'
    print(f"Adding {sample1_a} and {sample1_b}: {add_numbers(sample1_a, sample1_b)}")

    sample2_a = 'five'
    sample2_b = 10
    print(f"Adding {sample2_a} and {sample2_b}: {add_numbers(sample2_a, sample2_b)}")