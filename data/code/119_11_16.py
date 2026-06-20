SWAP_MULTIPLIER = 10

def reverse_numbers(a, b):
    a += SWAP_MULTIPLIER * b
    b = (a - b) / SWAP_MULTIPLIER
    a -= b * SWAP_MULTIPLIER
    return int(a), int(b)

if __name__ == '__main__':
    num1 = 30
    num2 = 75
    result = reverse_numbers(num1, num2)
    print(result)