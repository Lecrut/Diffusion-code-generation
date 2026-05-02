def calculate_perimeter(side_lengths):
    if not side_lengths:
        return 0
    return sum(side_lengths)
if __name__ == '__main__':
    sample1 = [3, 4, 5]
    sample2 = []
    sample3 = [10, 20, 30, 40]
    sample4 = []
    print(calculate_perimeter(sample1))
    print(calculate_perimeter(sample2))
    print(calculate_perimeter(sample3))
    print(calculate_perimeter(sample4))