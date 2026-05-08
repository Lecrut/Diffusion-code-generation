def parity(n):
    return n & 1
if __name__ == '__main__':
    num1 = 7
    num2 = 10
    num3 = 0
    print(f"Parity of {num1}: {parity(num1)}")
    print(f"Parity of {num2}: {parity(num2)}")
    print(f"Parity of {num3}: {parity(num3)}")