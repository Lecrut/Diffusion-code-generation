from typing import List
def tally_items(sequence: List[int]) -> int:
    count = 0
    for index in range(len(sequence)):
        if sequence[index] > 0:
            count += 1
    return count
if __name__ == '__main__':
    sample_data = [3, -2, 5, 0, 7, 4]
    result = tally_items(sample_data)
    print(result)