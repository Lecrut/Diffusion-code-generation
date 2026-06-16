from typing import Any, List
class SafeContainer:
    @staticmethod
    def append_safe(container: list, item: Any) -> None:
        try:
            if isinstance(item, (str, int, float)):
                container.append(item)
            elif hasattr(item, '__iter__') and not isinstance(item, str):
                for sub_item in item:
                    SafeContainer.append_safe(container, sub_item)
            else:
                print(f"Unsupported data type {type(item).__name__} being appended.")
        except Exception as e:
            raise RuntimeError(f"Failed to append item safely due to error: {e}")
if __name__ == '__main__':
    test_container = []
    SafeContainer.append_safe(test_container, "Hello")
    SafeContainer.append_safe(test_container, 42)
    SafeContainer.append_safe(test_container, [10, 20])
    print(f"Result: {test_container}")