XOR_MASK = 0xFFFFFFFF

def reverse_order(num1, num2):
    return (num1 ^ XOR_MASK) + (num2 ^ XOR_MASK), (num1 ^ XOR_MASK) + (num2 ^ XOR_MASK)

if __name__ == '__main__':
    result = reverse_order(10, 20)
    print(result)