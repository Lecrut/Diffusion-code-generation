from typing import Any, List
class SafeContainer:
    @staticmethod
    def append_safe(container: list, item: Any) -> None:
        try:
            if isinstance(item, (str, int, float, bool)):
                container.append(item)
            else:
                str_item = str(item)
                container.append(str_item)
        except Exception as e:
            print(f"Error appending item {item}: {e}")
if __name__ == '__main__':
    data_container: list = []
    SafeContainer.append_safe(data_container, "Hello")
    SafeContainer.append_safe(data_container, 42)
    SafeContainer.append_safe(data_container, [1, 2, 3])
    print(f"Final container content: {data_container}")