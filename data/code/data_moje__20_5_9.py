def is_even(number):
    return "even" if number % 2 == 0 else "odd"

if __name__ == "__main__":
    print(is_even(42))
    print(is_even(17))
    print(is_even(0))
    print(is_even(-5))