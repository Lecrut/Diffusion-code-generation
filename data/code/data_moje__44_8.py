def compute_mean(data: list[int]) -> float:
    if not data:
        raise ValueError("List must not be empty")
    total = 0
    for item in data:
        if not isinstance(item, int):
            raise TypeError(f"Expected integer, got {type(item)}")
        total += item
    return total / len(data)

if __name__ == '__main__':
    values = [10, 20, 30, 40, 50]
    result = compute_mean(values)
    print(result)