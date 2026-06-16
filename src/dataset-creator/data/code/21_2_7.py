from typing import Any
def safe_append(container: list[Any], item: Any) -> None:
    try:
        if not isinstance(item, (str, int, float)):
            raise TypeError(f"Unsupported operation for {type(item).__name__}")
        container.append(item)
    except Exception as e:
        print(f"Error appending item: {e}")
if __name__ == '__main__':
    data_container = []
    safe_append(data_container, "Hello")
    safe_append(data_container, 42)
    safe_append(data_container, 3.14)