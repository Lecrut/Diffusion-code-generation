import random

ROW_META = {
    0: "alpha",
    1: "beta",
    2: "gamma",
    3: "delta"
}

def _validate_matrix(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list of lists")

def _get_category(index):
    return ROW_META.get(index, "unknown")

def select_random_row(data):
    _validate_matrix(data)
    max_idx = len(data) - 1
    chosen_idx = random.randint(0, max_idx)
    category_name = _get_category(chosen_idx)
    row_content = data[chosen_idx]
    return {
        "index": chosen_idx,
        "category": category_name,
        "row": row_content
    }

if __name__ == '__main__':
    dataset = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
        [100, 110, 120]
    ]
    output = select_random_row(dataset)
    print(output)