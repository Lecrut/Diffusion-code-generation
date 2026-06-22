def compare_cm_lengths(length1: float, length2: float) -> str:
    shorter_length = min(length1, length2)
    return f"{shorter_length} cm"

if __name__ == '__main__':
    sample1 = compare_cm_lengths(50.0, 75.0)
    print(sample1)
    
    sample2 = compare_cm_lengths(3.0, 2.5)
    print(sample2)