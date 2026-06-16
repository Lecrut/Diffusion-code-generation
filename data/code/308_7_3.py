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
    sequence1 = [1, 2, 2, 3, 2, 2, 2, 4]
    element1 = 2
    result1 = count_consecutive(sequence1, element1)
    print(f"Sequence: {sequence1}, Element: {element1}, Count: {result1}")
    sequence2 = ['a', 'a', 'a', 'b', 'a', 'a']
    element2 = 'a'
    result2 = count_consecutive(sequence2, element2)
    print(f"Sequence: {sequence2}, Element: {element2}, Count: {result2}")
    sequence3 = [1, 1, 1, 1]
    element3 = 1
    result3 = count_consecutive(sequence3, element3)
    print(f"Sequence: {sequence3}, Element: {element3}, Count: {result3}")
    sequence4 = [5, 6, 7, 8]
    element4 = 5
    result4 = count_consecutive(sequence4, element4)
    print(f"Sequence: {sequence4}, Element: {element4}, Count: {result4}")
    sequence5 = [1, 2, 3, 4, 5]
    element5 = 9
    result5 = count_consecutive(sequence5, element5)
    print(f"Sequence: {sequence5}, Element: {element5}, Count: {result5}")
    sequence6 = [1, 1, 2, 2, 2, 3, 3, 3, 3]
    element6 = 3
    result6 = count_consecutive(sequence6, element6)
    print(f"Sequence: {sequence6}, Element: {element6}, Count: {result6}")