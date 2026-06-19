LENGTH_CONSTANT = 1

def compute_length_ratio(length_a, length_b):
    smaller_length = min(length_a, length_b)
    larger_length = max(length_a, length_b)
    ratio = larger_length / smaller_length * LENGTH_CONSTANT
    return ratio

if __name__ == '__main__':
    length1 = 20
    length2 = 50
    ratio_result = compute_length_ratio(length1, length2)
    print(ratio_result)