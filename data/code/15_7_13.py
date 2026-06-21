from typing import List, Any

def get_second_last_element(data: List[Any]) -> Any:
    if len(data) < 2:
        raise ValueError("List must contain at least two elements")
    return data[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_last_element(sample_list)
    print(result)