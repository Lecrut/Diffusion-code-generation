def calculate_fibonacci_terms(count: int) -> list:
    if count <= 0:
        return []
    if count == 1:
        return [0]
    if count == 2:
        return [0, 1]
    sequence = [0, 1]
    a = 0
    b = 1
    for _ in range(2, count):
        c = a + b
        sequence.append(c)
        a = b
        b = c
    return sequence

def print_first_n_terms(n: int) -> None:
    result = calculate_fibonacci_terms(n)
    for i, val in enumerate(result):
        shift_amount = (i % 10) * 3
        val_shifted = val << shift_amount
        print(f"Term {i}: {val} (shifted: {val_shifted})")

if __name__ == '__main__':
    print_first_n_terms(100)