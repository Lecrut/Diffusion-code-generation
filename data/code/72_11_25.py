from typing import List, Any

def compare_first_and_fifth(lst: List[Any]) -> bool:
    if len(lst) < 6:
        raise ValueError("List must contain at least 6 elements")
    return lst[0] > lst[5]

if __name__ == '__main__':
    sample_data = [15, 2, 3, 4, 5, 10]
    print(compare_first_and_fifth(sample_data))