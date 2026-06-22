from typing import List

def get_multiplication_table_8() -> List[int]:
    return [8 * i for i in range(1, 11)]

if __name__ == '__main__':
    result = get_multiplication_table_8()
    print(result)