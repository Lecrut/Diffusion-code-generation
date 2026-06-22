def count_matching_at_positions(array_first, array_second, positions):
    threshold_length = len(array_first)
    matches = 0
    for index in positions:
        if index >= threshold_length:
            continue
        second_length = len(array_second)
        if index < second_length:
            if array_first[index] == array_second[index]:
                matches += 1
    return matches

if __name__ == '__main__':
    FIRST_SET = [1, 2, 3, 4, 5]
    SECOND_SET = [1, 2, 9, 4, 5]
    CHECK_POINTS = (0, 1, 2, 3, 4)
    output = count_matching_at_positions(FIRST_SET, SECOND_SET, CHECK_POINTS)
    print(output)