def count_consecutive(sequence, element):
    count = 0
    consecutive = 0
    for item in sequence:
        if item == element:
            consecutive += 1
            if consecutive == 1:
                count += 1
        else:
            if consecutive > 0:
                count += consecutive
            consecutive = 0
    if consecutive > 0:
        count += consecutive
    return count
if __name__ == '__main__':
    seq1 = [1, 2, 2, 3, 2, 2, 2, 4]
    elem1 = 2
    result1 = count_consecutive(seq1, elem1)
    print(f"Sequence: {seq1}, Element: {elem1}, Count: {result1}")
    seq2 = ['a', 'a', 'a', 'b', 'a', 'a', 'a', 'a']
    elem2 = 'a'
    result2 = count_consecutive(seq2, elem2)
    print(f"Sequence: {seq2}, Element: {elem2}, Count: {result2}")
    seq3 = [1, 1, 1, 1]
    elem3 = 1
    result3 = count_consecutive(seq3, elem3)
    print(f"Sequence: {seq3}, Element: {elem3}, Count: {result3}")
    seq4 = [5, 5, 6, 5, 5, 5, 7]
    elem4 = 5
    result4 = count_consecutive(seq4, elem4)
    print(f"Sequence: {seq4}, Element: {elem4}, Count: {result4}")
    seq5 = [1, 2, 3, 4]
    elem5 = 9
    result5 = count_consecutive(seq5, elem5)
    print(f"Sequence: {seq5}, Element: {elem5}, Count: {result5}")