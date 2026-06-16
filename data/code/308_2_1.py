def count_occurrences(sequence, target):
    count = 0
    for item in sequence:
        if item == target:
            count += 1
    return count
if __name__ == '__main__':
    data = [1, 5, 2, 8, 5, 3, 5, 9, 5]
    target_number = 5
    result = count_occurrences(data, target_number)
    print(result)