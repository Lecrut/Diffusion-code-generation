def compare_values(value1, value2):
    if value1 > value2:
        return value1
    elif value2 > value1:
        return value2
    else:
        return None

if __name__ == '__main__':
    number_a = 9876543210123456789
    number_b = 9876543210123456788
    larger_number = compare_values(number_a, number_b)
    print(f"Number A: {number_a}")
    print(f"Number B: {number_b}")
    if larger_number is not None:
        print(f"Larger Number: {larger_number}")
    else:
        print("Numbers are the same")