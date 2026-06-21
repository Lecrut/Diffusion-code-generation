from typing import List

def calculate_differences(list1: List[float], list2: List[float]) -> List[float]:
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    differences = [a - b for a, b in zip(list1, list2)]
    return differences

if __name__ == '__main__':
    sample_list1 = [3.5, 6.7, 9.8]
    sample_list2 = [1.2, 4.5, 7.8]
    
    result = calculate_differences(sample_list1, sample_list2)
    print(result)