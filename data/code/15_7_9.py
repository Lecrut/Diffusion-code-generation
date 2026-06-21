from typing import Any, List, Optional

def get_second_last_element(items: List[Any]) -> Optional[Any]:
    if len(items) < 2:
        return None
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_last_element(sample_list)
    print(result)