from typing import List, Any

def get_second_last(items: List[Any]) -> Any:
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_last(sample_list)
    print(result)