from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list_end(lst: List[T], *items: T) -> None:
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    for item in items:
        try:
            lst.append(item)
        except Exception as e:
            raise RuntimeError(f"Failed to append element {item}: {e}")
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    extend_list_end(sample_list, "a", True, None)
    print("Extended list:", sample_list)