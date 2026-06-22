MAX_FACTORIAL_EXAMPLE = 20

def factorial(count):
    current = 1
    index = 2
    while index <= count:
        current *= index
        index += 1
    return current

if __name__ == "__main__":
    target = MAX_FACTORIAL_EXAMPLE
    computed = factorial(target)
    print(computed)