from typing import Any, List
class SafeContainer:
    @staticmethod
    def append_safe(container: List[Any], item: Any) -> None:
        try:
            container.append(item)
        except Exception as e:
            pass
if __name__ == '__main__':
    my_list = [1, "two", 3.0]
    SafeContainer.append_safe(my_list, None)
    SafeContainer.append_safe(my_list, True)
    SafeContainer.append_safe(my_list, {"key": "value"})
    print(f"Result: {my_list}")