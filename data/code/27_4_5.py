from typing import Tuple, List, Union

def validate_triangle(sides: Tuple[Union[int, float], Union[int, float], Union[int, float]]) -> bool:
    if len(sides) != 3:
        return False
    
    a, b, c = sides
    
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    
    return True

def evaluate_multiple_configurations(configurations: List[Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> List[bool]:
    return [validate_triangle(sides) for sides in configurations]

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 10, 10),
        (0, 1, 2),
        (1, 1, 3),
        (5.5, 5.5, 5.5),
        (-1, 2, 3)
    ]
    
    results = evaluate_multiple_configurations(test_cases)
    
    for sides, is_valid in zip(test_cases, results):
        print(f"{sides}: {is_valid}")