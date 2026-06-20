from typing import Union

def lengths_equal_within_threshold(len1: int, len2: int, threshold: int) -> bool:
    if threshold < 0:
        raise ValueError("Threshold must be non-negative")
    return abs(len1 - len2) <= threshold

if __name__ == '__main__':
    sample_length1 = 100
    sample_length2 = 102
    sample_threshold = 5
    print(lengths_equal_within_threshold(sample_length1, sample_length2, sample_threshold))
    print(lengths_equal_within_threshold(50, 60, 5))