MAX_SET_SIZE = 100

def compare_sets(set_a, set_b):
    if len(set_a) > MAX_SET_SIZE or len(set_b) > MAX_SET_SIZE:
        raise ValueError("One of the sets is too large")
    return max(set_a, set_b, key=len)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3}
    sample_set2 = {4, 5, 6, 7}
    larger_set = compare_sets(sample_set1, sample_set2)
    print(larger_set)