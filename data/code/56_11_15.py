from typing import List

TABLE_NUMBER: int = 7
TABLE_LIMIT: int = 10
ROW_SEPARATOR: str = '\n'
MULTIPLICATION_SYMBOL: str = ' x '
EQUATION_SEPARATOR: str = ' = '

def _build_row(factor: int) -> str:
    result_value: int = TABLE_NUMBER * factor
    return f"{TABLE_NUMBER}{MULTIPLICATION_SYMBOL}{factor}{EQUATION_SEPARATOR}{result_value}"

def generate_seven_table() -> str:
    rows: List[str] = []
    current_factor: int = 1
    while current_factor <= TABLE_LIMIT:
        rows.append(_build_row(current_factor))
        current_factor += 1
    return ROW_SEPARATOR.join(rows)

if __name__ == '__main__':
    output: str = generate_seven_table()
    print(output)