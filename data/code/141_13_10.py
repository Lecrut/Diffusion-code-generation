class BitwiseOperations:
    @staticmethod
    def and_gate(a, b):
        return a & b

    @staticmethod
    def or_gate(a, b):
        return a | b

    @staticmethod
    def not_gate(a):
        return ~a + 2 if a >= 0 else ~(a - 1)

if __name__ == '__main__':
    bitwise_ops = BitwiseOperations()
    
    print("Testing AND gate:")
    a_val = 5
    b_val = 3
    print(f"AND({a_val}, {b_val}) = {bitwise_ops.and_gate(a_val, b_val)}")
    a_val = 7
    b_val = 10
    print(f"AND({a_val}, {b_val}) = {bitwise_ops.and_gate(a_val, b_val)}")
    
    print("\nTesting OR gate:")
    a_val = 5
    b_val = 3
    print(f"OR({a_val}, {b_val}) = {bitwise_ops.or_gate(a_val, b_val)}")
    a_val = 7
    b_val = 10
    print(f"OR({a_val}, {b_val}) = {bitwise_ops.or_gate(a_val, b_val)}")
    
    print("\nTesting NOT gate:")
    a_val = 5
    print(f"NOT({a_val}) = {bitwise_ops.not_gate(a_val)}")
    a_val = -3
    print(f"NOT({a_val}) = {bitwise_ops.not_gate(a_val)}")