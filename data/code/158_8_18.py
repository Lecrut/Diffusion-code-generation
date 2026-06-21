from itertools import islice

def extract_even_numbers(data):
    return list(islice(data, 1, None, 2))

if __name__ == '__main__':
    sample_range_1 = range(1, 31)
    even_numbers_1 = extract_even_numbers(sample_range_1)
    print(f"Range: {sample_range_1}")
    print(f"Even numbers: {even_numbers_1}")

    sample_range_2 = range(50, 81)
    even_numbers_2 = extract_even_numbers(sample_range_2)
    print(f"Range: {sample_range_2}")
    print(f"Even numbers: {even_numbers_2}")