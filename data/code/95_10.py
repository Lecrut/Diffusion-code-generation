def check_number(number):
    is_positive = number > 0
    is_even = number % 2 == 0
    is_less_than_100 = number < 100
    if is_positive and is_even and is_less_than_100:
        print(f"The number {number} is positive, even, and less than 100.")
    elif not is_positive:
        print(f"The number {number} is not positive.")
    elif not is_even:
        print(f"The number {number} is not even.")
    elif not is_less_than_100:
        print(f"The number {number} is not less than 100.")
    else:
        print(f"The number {number} does not meet all the specified criteria.")
if __name__ == '__main__':
    test_numbers = [10, 15, 200, -5, 42]
    for num in test_numbers:
        check_number(num)