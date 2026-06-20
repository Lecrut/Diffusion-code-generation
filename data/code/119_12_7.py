def reverse_order(a, b):
    return b ^ (a ^ b), a ^ (b ^ a)

if __name__ == '__main__':
    result = reverse_order(5, 3)
    print(result)