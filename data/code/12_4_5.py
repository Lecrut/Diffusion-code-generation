def middle_value(sequence):
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    if n % 2 == 1:
        return sorted_seq[n // 2]
    else:
        mid1 = sorted_seq[n // 2 - 1]
        mid2 = sorted_seq[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    example1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    example2 = [10, 20, 30, 40]
    
    result1 = middle_value(example1)
    result2 = middle_value(example2)
    
    print(result1)
    print(result2)