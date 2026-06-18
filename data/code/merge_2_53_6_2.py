def tally_items(sequence: list) -> int:
    count = 0
    for index in range(len(sequence)):
        if sequence[index] is not None:
            count += 1
    return count
if __name__ == '__main__':
    sample_data = [None, "apple", "", "banana", None, "cherry"]
    result = tally_items(sample_data)
    print(result)