from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list(lst: List[T], *elements: T) -> None:
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    for element in elements:
        try:
            lst.append(element)
        except Exception as e:
            print(f"Error appending {element}: {e}")
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    extend_list(sample_list, "a", True, None)