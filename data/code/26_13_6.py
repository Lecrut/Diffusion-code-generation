from typing import List, Any

def check_first_greater_than_second(lst: List[Any]) -> bool:
    return lst[0] > lst[1] if len(lst) >= 2 else False

if __name__ == '__main__':
    sample_list = [5, 3, 8]
    result = check_first_greater_than_second(sample_list)
    print(result)