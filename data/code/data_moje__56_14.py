def get_multiplication_table(number: int) -> list[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

if __name__ == '__main__':
    print('\n'.join(get_multiplication_table(4)))