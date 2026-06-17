def count_consecutive(sequence, element):
    count = 0
    for item in sequence:
        if item == element:
            count += 1
        else:
            if count > 0:
                return count
            count = 0
    if count > 0:
        return count
    return 0
if __name__ == '__main__':
    sequence1 = [1, 2, 2, 2, 3, 2]
    element1 = 2
    result1 = count_consecutive(sequence1, element1)
    print(f"Sequence: {sequence1}, Element: {element1}, Count: {result1}")
    sequence2 = [5, 5, 5, 6, 7, 7]
    element2 = 5
    result2 = count_consecutive(sequence2, element2)
    print(f"Sequence: {sequence2}, Element: {element2}, Count: {result2}")
    sequence3 = [1, 2, 3, 4, 5]
    element3 = 9
    result3 = count_consecutive(sequence3, element3)
    print(f"Sequence: {sequence3}, Element: {element3}, Count: {result3}")
    sequence4 = [8, 8, 8, 8, 1]
    element4 = 8
    result4 = count_consecutive(sequence4, element4)
    print(f"Sequence: {sequence4}, Element: {element4}, Count: {result4}")
    sequence5 = [1, 2, 1, 1, 3]
    element5 = 1
    result5 = count_consecutive(sequence5, element5)
    print(f"Sequence: {sequence5}, Element: {element5}, Count: {result5}")
    sequence6 = [4, 4, 4, 4]
    element6 = 4
    result6 = count_consecutive(sequence6, element6)
    print(f"Sequence: {sequence6}, Element: {element6}, Count: {result6}")