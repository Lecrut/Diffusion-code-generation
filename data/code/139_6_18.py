class LogicGates:
    @staticmethod
    def and_gate(a, b):
        if isinstance(a, str) and all(c in '01' for c in a):
            a_val = int(a, 2)
        elif isinstance(a, int):
            a_val = a
        else:
            raise TypeError("Invalid type for input a")
        
        if isinstance(b, str) and all(c in '01' for c in b):
            b_val = int(b, 2)
        elif isinstance(b, int):
            b_val = b
        else:
            raise TypeError("Invalid type for input b")
        
        return a_val & b_val

    @staticmethod
    def or_gate(a, b):
        if isinstance(a, str) and all(c in '01' for c in a):
            a_val = int(a, 2)
        elif isinstance(a, int):
            a_val = a
        else:
            raise TypeError("Invalid type for input a")
        
        if isinstance(b, str) and all(c in '01' for c in b):
            b_val = int(b, 2)
        elif isinstance(b, int):
            b_val = b
        else:
            raise TypeError("Invalid type for input b")
        
        return a_val | b_val

    @staticmethod
    def not_gate(a):
        if isinstance(a, str) and all(c in '01' for c in a):
            a_val = int(a, 2)
        elif isinstance(a, int):
            a_val = a
        else:
            raise TypeError("Invalid type for input a")
        
        return ~a_val

    @staticmethod
    def xor_gate(a, b):
        if isinstance(a, str) and all(c in '01' for c in a):
            a_val = int(a, 2)
        elif isinstance(a, int):
            a_val = a
        else:
            raise TypeError("Invalid type for input a")
        
        if isinstance(b, str) and all(c in '01' for c in b):
            b_val = int(b, 2)
        elif isinstance(b, int):
            b_val = b
        else:
            raise TypeError("Invalid type for input b")
        
        return a_val ^ b_val

if __name__ == '__main__':
    print(LogicGates.and_gate("101", "110"))
    print(LogicGates.or_gate(1, 0))
    print(LogicGates.not_gate("1"))
    print(LogicGates.xor_gate("101", "011"))