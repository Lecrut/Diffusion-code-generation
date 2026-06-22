from typing import List

def calculate_differences(list1: List[float], list2: List[float]) -> List[float]:
    differences = []
    for a in list1:
        for b in list2:
            difference = abs(a - b)
            differences.append(difference)
    return differences

if __name__ == '__main__':
    LIST1_SAMPLE = [1.5, 3.2, 7.8]
    LIST2_SAMPLE = [2.1, 4.4, 6.9]
    result = calculate_differences(LIST1_SAMPLE, LIST2_SAMPLE)
    print(result)