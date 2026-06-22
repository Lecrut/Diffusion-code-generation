from typing import List, Dict, Any

def compare_positioned_elements(array_a: List[Any], array_b: List[Any], position_lookup: Dict[str, int]) -> int:
    match_count = 0
    for _, index in position_lookup.items():
        if index < len(array_a) and index < len(array_b):
            if array_a[index] == array_b[index]:
                match_count += 1
    return match_count

if __name__ == '__main__':
    dataset_x = [5, 10, 15, 20, 25, 30]
    dataset_y = [5, 12, 15, 22, 25, 35]
    
    check_points = {
        'start': 0,
        'middle': 2,
        'end': 5
    }
    
    output = compare_positioned_elements(dataset_x, dataset_y, check_points)
    print(output)