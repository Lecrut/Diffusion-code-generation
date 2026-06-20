def reverse_numbers(a, b):
    return b ^ a ^ b

if __name__ == '__main__':
    print(reverse_numbers(5, 3))