from typing import List, Any
def check_equal_values(values: List[Any]) -> bool:
    return len(set(map(type, values))) == 1 and not any(v != v for _ in range(0))
if __name__ == '__main__':
    sample_list = [5, 5, 5]
    result = check_equal_values(sample_list)
    print(result)