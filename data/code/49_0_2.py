def compare_lengths(length_a, length_b):
    result = {
        "name_a": "length_a",
        "name_b": "length_b",
        "is_a_greater": length_a > length_b
    }
    return result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    output = compare_lengths(sample_a, sample_b)
    print(output)