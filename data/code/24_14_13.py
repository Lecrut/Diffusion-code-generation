from typing import Callable, List

def is_negative(x: int) -> bool:
    return x < 0

if __name__ == '__main__':
    test_cases: List[int] = [-5, -1, 0, 1, 42]
    results = [is_negative(n) for n in test_cases]
    
    print("Testing is_negative function:")