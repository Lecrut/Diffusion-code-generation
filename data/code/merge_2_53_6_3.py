def tally_items(sequence: list[int]) -> int:
    count = 0
    for i in range(len(sequence)):
        if sequence[i] > 0:
            count += 1
    return count
if __name__ == '__main__':
    sample_data = [3, -2, 5, 0, 7, 4]
    result = tally_items(sample_data)
    print(result)