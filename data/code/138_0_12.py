class LogicTruthTable:
    AND_TABLE = {
        (True, True): True,
        (True, False): False,
        (False, True): False,
        (False, False): False
    }
    
    OR_TABLE = {
        (True, True): True,
        (True, False): True,
        (False, True): True,
        (False, False): False
    }
    
    XOR_TABLE = {
        (True, True): False,
        (True, False): True,
        (False, True): True,
        (False, False): False
    }
    
    @staticmethod
    def generate_truth_table(operation):
        if operation == 'AND':
            return LogicTruthTable.AND_TABLE.items()
        elif operation == 'OR':
            return LogicTruthTable.OR_TABLE.items()
        elif operation == 'XOR':
            return LogicTruthTable.XOR_TABLE.items()
        else:
            raise ValueError("Invalid operation")

if __name__ == '__main__':
    operations = ['AND', 'OR', 'XOR']
    for op in operations:
        print(f"Truth Table for {op}:")
        table = LogicTruthTable.generate_truth_table(op)
        for inputs, result in table:
            print(f"A: {inputs[0]}, B: {inputs[1]} -> A {op} B: {result}")