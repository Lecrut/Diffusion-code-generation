SWAP_CONST = True

def reverse_numbers(a, b):
    return (b, a) if SWAP_CONST else (a, b)

if __name__ == '__main__':
    print(reverse_numbers(3, 5))