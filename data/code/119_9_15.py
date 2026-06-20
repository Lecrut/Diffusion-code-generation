class Reverser:
    @staticmethod
    def reverse(a, b):
        return b, a

if __name__ == '__main__':
    original_a = 10
    original_b = 20
    reversed_a, reversed_b = Reverser.reverse(original_a, original_b)
    print(f"Before reversal: a={original_a}, b={original_b}")
    print(f"After reversal: a={reversed_a}, b={reversed_b}")