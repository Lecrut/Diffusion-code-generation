class ZeroVerifier:
    def __init__(self, numbers):
        self.numbers = numbers

    def contains_zero(self):
        return any(num == 0 for num in self.numbers)

if __name__ == '__main__':
    verifier1 = ZeroVerifier([1, 2, 3, 4, 5])
    verifier2 = ZeroVerifier([1, 0, 3, 4, 5])
    verifier3 = ZeroVerifier([10, 20, 30])

    print("Verifier 1 contains zero:", verifier1.contains_zero())
    print("Verifier 2 contains zero:", verifier2.contains_zero())
    print("Verifier 3 contains zero:", verifier3.contains_zero())