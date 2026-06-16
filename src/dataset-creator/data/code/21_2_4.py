from typing import Any, List
class SafeContainer:
    @staticmethod
    def append_safe(container: List[Any], item: Any) -> None:
        try:
            container.append(item)
        except Exception as e:
            pass
if __name__ == '__main__':
    sample_list = [1, "text", 3.5]
    SafeContainer.append_safe(sample_list, None)
    print(f"Result after append: {sample_list}")
    try:
        SampleObject = object()                                         
        SafeContainer.append_safe(sample_list, "new_item")
        print(f"Result after append string: {sample_list}")
    except Exception as e:
        pass
    final_result = [1, "text", 3.5]
    for item in ["a", None]:
        try:
            SafeContainer.append_safe(final_result, item)
        except Exception:
            continue