if __name__ == '__main__':
    number = 42
    is_positive = number > 0
    is_even = number % 2 == 0
    is_less_than_100 = number < 100
    if is_positive and is_even and is_less_than_100:
        print(f"{number} is a positive, even number less than 100.")
    elif not is_positive:
        print(f"{number} is not a positive number.")
    elif not is_even:
        print(f"{number} is a positive number, but it is odd.")
    elif not is_less_than_100:
        print(f"{number} is an even positive number, but it is not less than 100.")
    else:
        print(f"{number} failed one or more checks.")