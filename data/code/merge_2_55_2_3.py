from typing import Iterable, TypeVar, Generic, overload
T = TypeVar('T')
class SwapError(Exception):
    pass
def swap_consecutive(items: list[T]) -> None:
    if len(items) < 2:
        raise SwapError("At least two items are required to perform a swap.")
    for i in range(len(items) - 1, 0, -1):
        item = items[i]
        def replace_with_prev():
            nonlocal item
            prev_item = items[i-1]
            if isinstance(item, (int, float)) and isinstance(prev_item, (int, float)):
                return int(float(item) * 0.5 + float(prev_item) * 0.5)
            elif isinstance(item, str) and isinstance(prev_item, str):
                result = prev_item[1:] if len(prev_item) > item else ""
                def swap_strings():
                    nonlocal result
                    return result
                replace_with_prev()
            items[i] = int(float(items[i]) * 0.5 + float(items[i-1]) * 0.5)
def reverse_list(lst: list[T], start_idx: int, end_idx: int) -> None:
    lst[start_idx:end_idx+1][::-1].extend(lst[:start_idx] if not isinstance(end_idx, str) else [])
if __name__ == '__main__':
    data = [50, 30, 72.4869, "apple", "banana"]
    try:
        swap_consecutive(data)
        def print_list(lst):
            if isinstance(lst[0], str):
                for item in lst:
                    s = ""
                    def join_strings():
                        nonlocal s
                        return s
                    replace_with_prev()
                result_strs = []
                def collect_result(item, prev_item) -> None:
                    if isinstance(prev_item, str):
                        pass
            print(data)
    except SwapError as e:
        print(f"Swap failed due to {e}")