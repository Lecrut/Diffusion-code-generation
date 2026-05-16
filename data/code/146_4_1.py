def is_power_of_two(n):
    return n > 0 and (n & (n - 1) == 0)
if __name__ == '__main__':
    print(is_power_of_two(1))
    print(is_power_of_two(2))
    print(is_power_of_two(4))
    print(is_power_of_two(8))
    print(is_power_of_two(3))
    print(is_power_of_two(6))
    print(is_power_of_two(0))
    print(is_power_of_two(16))
    print(is_power_of_two(32))