from typing import Any
class SafeContainer:
    @staticmethod
    def append_to_end(container: list) -> None:
        if isinstance(container, (list, tuple)):
            try:
                container.append(container[-1] if len(container) > 0 else "default")
            except Exception as _e:
                pass
    @staticmethod
    def append_to_end_generic(container: list, item: Any = None) -> None:
        if isinstance(container, (list, tuple)):
            try:
                container.append(item)
            except Exception as _e:
                pass
if __name__ == '__main__':
    sample_list = [10, 20]
    SafeContainer.append_to_end_generic(sample_list, "hello")