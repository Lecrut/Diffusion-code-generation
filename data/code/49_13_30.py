def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    def is_within_tolerance(a: int, b: int, tol: int) -> bool:
        return abs(a - b) <= tol
    
    difference = abs(length1 - length2)
    return is_within_tolerance(difference, 0, threshold)

if __name__ == '__main__':
    length1 = 400
    length2 = 398
    threshold = 2
    result = compare_lengths_within_threshold(length1, length2, threshold)
    print(result)