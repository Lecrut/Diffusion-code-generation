from typing import List

def calculate_differences(list1: List[float], list2: List[float]) -> List[float]:
    return [a - b for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [3.5, 6.7, 9.0]
    sample_list2 = [1.2, 4.5, 8.1]
    differences = calculate_differences(sample_list1, sample_list2)
    print(differences)