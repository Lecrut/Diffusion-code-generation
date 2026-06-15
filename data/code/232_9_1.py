def print_powers_of_two(n=10, current_power=0):
    if current_power > n:
        return
    print(2**current_power)
    print_powers_of_two(n, current_power + 1)
if __name__ == '__main__':
    print_powers_of_two(10)