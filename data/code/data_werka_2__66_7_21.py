def check_ascending_adjacent(elements):
    return [elements[i] < elements[i + 1] for i in range(len(elements) - 1)]

if __name__ == '__main__':
    test_sequence = [5, 7, 6, 8, 9]
    ascending_status = check_ascending_adjacent(test_sequence)
    print(ascending_status)