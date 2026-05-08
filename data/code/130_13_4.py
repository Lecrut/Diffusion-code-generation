def check_for_zero(numbers):
    for number in numbers:
        if number == 0:
            yield True
            return
if __name__ == '__main__':
    sequence1 = [1, 2, 3, 4, 5]
    sequence2 = [1, 0, 3, 4, 5]
    sequence3 = [10, 20, 30]
    sequence4 = [7, 8, 0, 9]
    sequence5 = []
    print("Sequence 1:", list(check_for_zero(sequence1)))
    print("Sequence 2:", list(check_for_zero(sequence2)))
    print("Sequence 3:", list(check_for_zero(sequence3)))
    print("Sequence 4:", list(check_for_zero(sequence4)))
    print("Sequence 5:", list(check_for_zero(sequence5)))