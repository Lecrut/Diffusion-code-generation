def count_consecutive(sequence, element):
    count = 0
    consecutive_count = 0
    for item in sequence:
        if item == element:
            consecutive_count += 1
            if consecutive_count == 1:
                count += 1
        else:
            if consecutive_count > 0:
                count += consecutive_count
            consecutive_count = 0
    if consecutive_count > 0:
        count += consecutive_count
    return count
if __name__ == '__main__':
    sequence1 = [1, 1, 2, 3, 3, 3, 4, 1]
    element1 = 3
    result1 = count_consecutive(sequence1, element1)
    print(f"Sequence: {sequence1}, Element: {element1}, Result: {result1}")
    sequence2 = ['a', 'a', 'a', 'b', 'a', 'a']
    element2 = 'a'
    result2 = count_consecutive(sequence2, element2)
    print(f"Sequence: {sequence2}, Element: {element2}, Result: {result2}")
    sequence3 = [5, 5, 5, 5]
    element3 = 5
    result3 = count_consecutive(sequence3, element3)
    print(f"Sequence: {sequence3}, Element: {element3}, Result: {result3}")
    sequence4 = [1, 2, 3, 4]
    element4 = 1
    result4 = count_consecutive(sequence4, element4)
    print(f"Sequence: {sequence4}, Element: {element4}, Result: {result4}")
    sequence5 = [1, 1, 1, 0, 1, 1]
    element5 = 1
    result5 = count_consecutive(sequence5, element5)
    print(f"Sequence: {sequence5}, Element: {element5}, Result: {result5}")
    sequence6 = [9, 8, 7, 8, 8, 8, 1]
    element6 = 8
    result6 = count_consecutive(sequence6, element6)
    print(f"Sequence: {sequence6}, Element: {element6}, Result: {result6}")