from typing import List, Any

def get_third_item(data: List[Any]) -> Any:
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) < 3:
        raise IndexError("List must contain at least three items")
    return data[2]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_item(sample_list)
    print(result)