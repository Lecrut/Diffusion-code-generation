def get_number_and_parity(n):
    return (n, n % 2 == 0)
if __name__ == '__main__':
    print(get_number_and_parity(4))
    print(get_number_and_parity(7))
    print(get_number_and_parity(0))
    print(get_number_and_parity(-3))