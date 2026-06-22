EVEN_THRESHOLD = 0

def is_even(number: int) -> bool:
    remainder = number % 2
    return remainder == EVEN_THRESHOLD

if __name__ == '__main__':
    print(is_even(10))
    print(is_even(11))
    print(is_even(0))
    print(is_even(-5))