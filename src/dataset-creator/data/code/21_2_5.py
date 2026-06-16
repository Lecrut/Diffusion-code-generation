from typing import Any
class SafeContainer:
    @staticmethod
    def append_to_end(container: list[Any], item: Any) -> None:
        try:
            if isinstance(item, (str, int, float, bool)):
                container.append(item)
            else:
                converted_item = item
                if not isinstance(converted_item, list):
                    converted_item = [converted_item]
                container.extend(converted_item)
        except Exception as e:
            pass
if __name__ == '__main__':
    data_container = []
    SafeContainer.append_to_end(data_container, "string")
    SafeContainer.append_to_end(data_container, 42)
    SafeContainer.append_to_end(data_container, [10, 20])
    print(f"Result: {data_container}")