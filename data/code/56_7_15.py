import math

def format_multiplication_table(base, rows=10):
    if base < 0:
        raise ValueError("Base must be non-negative")
    if rows < 1:
        raise ValueError("Rows must be at least 1")
    
    max_val = base * (rows - 1)
    width = len(str(max_val)) + 2
    header_width = width
    
    header_parts = [" " * header_width]
    for i in range(1, rows + 1):
        header_parts.append(f"{i:>{width}}")
    print("".join(header_parts))
    
    for i in range(1, rows + 1):
        row_parts = [f"{i:>{header_width}}"]
        for j in range(1, rows + 1):
            value = i * j
            row_parts.append(f"{value:>{width}}")
        print("".join(row_parts))

if __name__ == '__main__':
    result = format_multiplication_table(9, 5)
    print(result)