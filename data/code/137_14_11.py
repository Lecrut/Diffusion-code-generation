EVEN_CHECK_MASK = 1

def is_even(number):
    return (number & EVEN_CHECK_MASK) == 0

if __name__ == '__main__':
    test_numbers = [2, 3, 4, -6, -7]
    for num in test_numbers:
        print(f"Number {num} is even: {is_even(num)}")