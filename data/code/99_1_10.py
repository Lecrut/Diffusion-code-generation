class OperatorPrecedence:

    def parse_expression(self, expression):
        return expression.split()
if __name__ == '__main__':
    op = OperatorPrecedence()
    result = op.parse_expression('a & b | c ^ d')
    print(result)