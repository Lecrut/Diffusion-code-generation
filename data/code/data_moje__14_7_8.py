from typing import Any, List

def get_third_item(items: List[Any]) -> Any:
    if len(items) < 3:
        raise IndexError("List must contain at least three items to retrieve the third item.")
    return items[2]

if __name__ == "__main__":
    sample_list = ["apple", "banana", "cherry", "date", "fig"]
    try:
        result = get_third_item(sample_list)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")

    short_list = ["one", "two"]
    try:
        result = get_third_item(short_list)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")