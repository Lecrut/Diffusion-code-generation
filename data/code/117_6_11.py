diff_table = {'a': 10, 'b': 5}

def calculate_difference(x: str, y: str) -> int:
    return diff_table[x] - diff_table[y]

if __name__ == '__main__':
    result = calculate_difference('a', 'b')
    print(result)