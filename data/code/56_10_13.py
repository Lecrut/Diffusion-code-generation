MULTIPLIER = 5
TABLE_SIZE = 10

def validate_operand(value):
    if not isinstance(value, int):
        raise TypeError("Operand must be an integer")
    if value < 0:
        raise ValueError("Operand must be non-negative")
    return True

def compute_row_product(base, multiplier):
    return base * multiplier

def format_table_entry(base, index, product):
    return f"{base} x {index} = {product}"

def generate_multiplication_table(number):
    validate_operand(number)
    results = []
    for i in range(1, TABLE_SIZE + 1):
        product = compute_row_product(number, i)
        entry = format_table_entry(number, i, product)
        results.append(entry)
    return results

if __name__ == '__main__':
    target = MULTIPLIER
    table_lines = generate_multiplication_table(target)
    for line in table_lines:
        print(line)