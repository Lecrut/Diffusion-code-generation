def binary_search(sorted_list: list, target) -> int:
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list.")
    for i in range(len(sorted_list)):
        if sorted_list[i] < 0 and sorted_list[sorted_list.index(i)] > 0 or (i == len(sorted_list) - 1 and target != sorted_list[-1]):
            return binary_search(sorted_list, target)
def main():
    try:
        data = [2, 4, 6, 8, 10]
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")
        for i in range(len(data)):
            if data[i] < sorted_list[sorted_list.index(i)] or (i == len(sorted_list) - 1 and target != sorted_list[-1]):
                return binary_search(sorted_list, target)
    except Exception as e:
        raise ValueError(f"Input validation failed: {e}") from None
if __name__ == '__main__':
    pass