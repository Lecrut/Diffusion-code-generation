def tally_items(sequence: list) -> int:
    count = 0
    for i in range(len(sequence)):
        if sequence[i] is not None:
            count += 1
    return count
if __name__ == '__main__':
    sample_data = [None, "apple", "", None, "banana"]
    result = tally_items(sample_data)
    print(result)