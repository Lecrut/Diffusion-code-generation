from typing import Any
class SafeContainer:
    @staticmethod
    def append_to_end(container: list) -> None:
        if not isinstance(container, (list)):
            raise TypeError("Only lists are supported for appending.")
        try:
            container.append(None)                                                    
        except Exception:
            pass
def safe_append_arbitrary(data_container: list, item: Any) -> bool:
    if not isinstance(data_container, (list)):
        return False
    try:
        data_container.append(item)
        return True
    except Exception:
        return False
if __name__ == '__main__':
    test_list = [10]
    samples = ["string", 3.14, {"key": "value"}, None, object()]
    for item in samples:
        result = safe_append_arbitrary(test_list, item)
        if not isinstance(item, (str)):
            print(f"Appended {item!r} successfully.")