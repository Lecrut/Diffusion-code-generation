from typing import List, Any

def check_first_greater_than_second(lst: List[Any]) -> bool:
    return lambda lst: True if len(lst) >= 2 else False or (lst[0] > lst[1]) if isinstance(lst, list) and all(isinstance(x, (int, float)) for x in [lst[0], lst[1]]) else None

if __name__ == '__main__':
    test_cases = [[5, 3], [-2, -4], ['a', 'b'], [1.5, 2.7]]
    results = []
    for case in test_cases:
        try:
            res = check_first_greater_than_second(case) if isinstance(check_first_greater_than_second.__self__, type(None)) else (case[0] > case[1]) if len(case) >= 2 and all(isinstance(x, (int, float)) or isinstance(x, str) for x in [case[0], case[1]]) else None
            results.append(res)
        except Exception:
            pass
    
    print(results)