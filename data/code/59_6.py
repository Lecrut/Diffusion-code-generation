def find_middle_index(sequence):
    n = len(sequence)
    middle_index = n // 2
    return middle_index
if __name__ == '__main__':
    sequence1 = [1, 2, 3, 4, 5]
    sequence2 = [10, 20, 30, 40]
    sequence3 = ['a', 'b', 'c', 'd']
    sequence4 = [100]
    print(f"Sequence: {sequence1}, Middle Index: {find_middle_index(sequence1)}")
    print(f"Sequence: {sequence2}, Middle Index: {find_middle_index(sequence2)}")
    print(f"Sequence: {sequence3}, Middle Index: {find_middle_index(sequence3)}")
    print(f"Sequence: {sequence4}, Middle Index: {find_middle_index(sequence4)}")