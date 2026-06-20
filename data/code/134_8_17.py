class BitwiseCounter:
    @staticmethod
    def count_true_bits(a, b, c, d, e):
        return (a + b + c + d + e) & 1

if __name__ == '__main__':
    print(BitwiseCounter.count_true_bits(True, False, True, False, False))