import sys

def calculate_ratio(length_a: float, length_b: float) -> float:
    """Calculate the ratio of two lengths (length_a / length_b)."""
    if length_b == 0:
        raise ValueError("Division by zero is not allowed.")
    return length_a / length_b

def format_table(rows_count: int, data_pairs: list[tuple[float, float]]) -> str:
    """Generate a formatted table string from the input pairs."""
    max_len_str = len(f"{data_pairs[0][0]:.2f}") if data_pairs else 1

    header = f"{'Index':<4} | {'Length A':>8}" + " | 'Length B':>" * (max_len_str) + "\n"
    separator = "-" * max(65, len(header.rstrip("\n")))

    lines = [header]
    for idx in range(rows_count):
        length_a, length_b = data_pairs[idx]
        ratio = calculate_ratio(length_a, length_b)

if __name__ == '__main__':
    pass
