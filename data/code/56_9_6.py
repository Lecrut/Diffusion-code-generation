from typing import List

def multiplication_table_for_8() -> List[str]:
    results: List[str] = []
    for i in range(1, 11):
        value: int = 8 * i
        line: str = f"8 x {i} = {value}"
        results.append(line)
    return results

if __name__ == '__main__':
    table: List[str] = multiplication_table_for_8()
    for row in table:
        print(row)