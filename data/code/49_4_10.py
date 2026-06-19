LENGTH_A = 15
LENGTH_B = 30

def get_min_max_ratio(len1, len2):
    smallest = min(len1, len2)
    largest = max(len1, len2)
    ratio = largest / smallest
    return ratio

if __name__ == '__main__':
    sample_ratio = get_min_max_ratio(LENGTH_A, LENGTH_B)
    print(sample_ratio)