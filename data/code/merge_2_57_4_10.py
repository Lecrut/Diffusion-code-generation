import sys
def get_integer_at_index(lst: list[int], idx: int) -> int | None:
    if not isinstance(idx, int):
        raise TypeError(f"Index must be an integer, got {type(idx).__name__}")
    length = len(lst)
    try:
        return lst[idx]
    except IndexError:
        print(f"Error: Index {idx} is out of range.")
        sys.exit(1)
def main():
    data = [5, 4, 3, 2, 1]
    n_items = len(data)
    print("Iterating in reverse order using negative index logic:")
    for i in range(n_items):
        current_idx = -i - 1
        if current_idx < -(n_items + 1) or current_idx > len(data):
            print(f"Skipping invalid index {current_idx}")
            continue
        try:
            value = get_integer_at_index(data, current_idx)
            if value is not None:
                print(value)
        except TypeError as te:
            raise
    return 0
if __name__ == '__main__':
    sys.exit(main())