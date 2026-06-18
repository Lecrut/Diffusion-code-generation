def is_even(number: int) -> bool:
    return not ((number & 1))
def main():
    test_values = [0, -3, 7, 100, -42]
    print("Parity Check Results:")
    for val in test_values:
        result = is_even(val)
        status = "Even" if result else "Odd"
        print(f"{val}: {status}")
if __name__ == '__main__':
    main()