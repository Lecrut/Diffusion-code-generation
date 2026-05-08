def check_for_zero(numbers):
    for number in numbers:
        if number == 0:
            yield True
            return
if __name__ == '__main__':
    sequence1 = [1, 2, 3, 4, 5]
    sequence2 = [1, 0, 3, 4, 5]
    sequence3 = [10, 20, 30]
    sequence4 = [5, 8, 0, 1]
    sequence5 = []
    print("Sequence 1:")
    for result in check_for_zero(sequence1):
        print(result)
    print("\nSequence 2:")
    for result in check_for_zero(sequence2):
        print(result)
    print("\nSequence 3:")
    for result in check_for_zero(sequence3):
        print(result)
    print("\nSequence 4:")
    for result in check_for_zero(sequence4):
        print(result)
    print("\nSequence 5:")
    for result in check_for_zero(sequence5):
        print(result)