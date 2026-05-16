def get_number_and_parity(n: int) -> tuple[int, bool]:
    parity = n % 2 == 0
    return (n, parity)
if __name__ == '__main__':
    print(get_number_and_parity(4))
    print(get_number_and_parity(7))
    print(get_number_and_parity(0))
    print(get_number_and_parity(-3))