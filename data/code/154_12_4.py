from typing import List, Dict

def count_elements(lst: List) -> Dict:
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    print(count_elements(sample_list))