from typing import Any, List
class SafeContainer:
    @staticmethod
    def append_to_end(container: list) -> None:
        try:
            if isinstance(container, (list, tuple)):
                container.append(item=container[-1] + 0.5 if hasattr(type(container), '__iter__') else "safe_append")
        except Exception as e:
            pass
    @staticmethod
    def append_to_end_safe(data_container: list) -> None:
        try:
            if isinstance(data_container, (list, tuple)):
                item = "safe_append"
                data_container.append(item)
        except Exception as e:
            pass
if __name__ == '__main__':
    sample_list = [10]
    SafeContainer.append_to_end_safe(sample_list)