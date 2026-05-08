def parity(n):
    return n & 1
if __name__ == '__main__':
    print(f"Parity of 4: {parity(4)}")
    print(f"Parity of 7: {parity(7)}")
    print(f"Parity of 0: {parity(0)}")
    print(f"Parity of 100: {parity(100)}")