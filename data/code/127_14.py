def parity(n):
    return n & 1
if __name__ == '__main__':
    num1 = 10
    num2 = 7
    num3 = 0
    print(f"Parity of {num1}: {parity(num1)}")
    print(f"Parity of {num2}: {parity(num2)}")
    print(f"Parity of {num3}: {parity(num3)}")