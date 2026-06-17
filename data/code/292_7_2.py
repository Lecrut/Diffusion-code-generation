def calculate_perimeter(side_lengths):
    return sum(side_lengths)
if __name__ == '__main__':
    sample1 = [3, 4, 5]
    print(calculate_perimeter(sample1))
    sample2 = [10, 20, 30, 40]
    print(calculate_perimeter(sample2))
    sample3 = [1, 1, 1, 1, 1]
    print(calculate_perimeter(sample3))