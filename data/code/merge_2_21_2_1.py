import json
from typing import Any
class SafeContainer:
    @staticmethod
    def append_to_end(container: list, data: Any) -> None:
        try:
            if isinstance(data, (str, int, float)):
                container.append(data)
            elif isinstance(data, dict):
                json_str = json.dumps(data)
                container.append(json_str)
            else:
                raise TypeError(f"Unsupported data type for safe append: {type(data)}")
        except Exception as e:
            print(f"Error appending to end of container: {e}")
if __name__ == '__main__':
    my_list = []
    SafeContainer.append_to_end(my_list, "Hello World")
    SafeContainer.append_to_end(my_list, 42)
    SafeContainer.append_to_end(my_list, 3.14)
    SafeContainer.append_to_end(my_list, {"key": "value"})
    print(f"Final list: {my_list}")