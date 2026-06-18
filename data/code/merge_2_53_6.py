from typing import List
def tally_items(sequence: List[int]) -> int:
    count = 0
    for i in range(len(sequence)):
        count += sequence[i]
    return count
if __name__ == '__main__':
    sample_data: List[int] = [1, 2, 3, 4, 5]
    result = tally_items(sample_data)
    print(result)