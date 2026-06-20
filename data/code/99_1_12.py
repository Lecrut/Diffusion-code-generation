class OperatorPrecedence:

    def parse_expression(self, expression):
        return expression
if __name__ == '__main__':
    op = OperatorPrecedence()
    result = op.parse_expression('3 & 5 | 2')
    print(result)