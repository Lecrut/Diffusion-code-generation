def is_power_of_two(n):
    return n > 0 and (n & (n - 1) == 0)
if __name__ == '__main__':
    print(f"1 is power of two: {is_power_of_two(1)}")
    print(f"2 is power of two: {is_power_of_two(2)}")
    print(f"4 is power of two: {is_power_of_two(4)}")
    print(f"8 is power of two: {is_power_of_two(8)}")
    print(f"3 is power of two: {is_power_of_two(3)}")
    print(f"6 is power of two: {is_power_of_two(6)}")
    print(f"0 is power of two: {is_power_of_two(0)}")
    print(f"1024 is power of two: {is_power_of_two(1024)}")
    print(f"1025 is power of two: {is_power_of_two(1025)}")