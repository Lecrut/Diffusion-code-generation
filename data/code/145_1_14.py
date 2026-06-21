class LogicalOperatorPrecedence:
    A = True
    B = False
    C = True

    @staticmethod
    def nested_logic():
        result1 = LogicalOperatorPrecedence.A and LogicalOperatorPrecedence.B or LogicalOperatorPrecedence.C
        result2 = not (LogicalOperatorPrecedence.A or LogicalOperatorPrecedence.B) and LogicalOperatorPrecedence.C
        return (result1, result2)
if __name__ == '__main__':
    output = LogicalOperatorPrecedence.nested_logic()
    print(output)