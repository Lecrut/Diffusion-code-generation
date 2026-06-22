from typing import List

def print_multiplication_table(value: int = 8) -> None:
    result: List[int] = []
    for i in range(1, 11):
        product: int = value * i
        result.append(product)
        print(f"{value} x {i} = {product}")

if __name__ == '__main__':
    print_multiplication_table(8)