class BitwiseOperations:
    @staticmethod
    def and_gate(a, b):
        return a & b

    @staticmethod
    def or_gate(a, b):
        return a | b

    @staticmethod
    def not_gate(a):
        return ~a & 1

if __name__ == '__main__':
    print("Testing AND gate:")
    a_val = 0b1100
    b_val = 0b1010
    print(f"AND({bin(a_val)}, {bin(b_val)}) = {BitwiseOperations.and_gate(a_val, b_val)}")

    print("\nTesting OR gate:")
    a_val = 0b1100
    b_val = 0b1010
    print(f"OR({bin(a_val)}, {bin(b_val)}) = {BitwiseOperations.or_gate(a_val, b_val)}")

    print("\nTesting NOT gate:")
    a_val = 0b1100
    print(f"NOT({bin(a_val)}) = {BitwiseOperations.not_gate(a_val)}")