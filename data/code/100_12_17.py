class LogicalStatementParser:

    def __init__(self):
        self.operators = {'AND': lambda x, y: x and y, 'OR': lambda x, y: x or y}

    def parse(self, statement, A, B):
        tokens = statement.split()
        if len(tokens) != 3 or tokens[1] not in self.operators:
            raise ValueError('Invalid logical statement format')
        return self.operators[tokens[1]](A, B)
if __name__ == '__main__':
    parser = LogicalStatementParser()
    print(parser.parse('A AND B', True, False))
    print(parser.parse('A OR B', False, False))
    print(parser.parse('A AND B', True, True))
    print(parser.parse('A OR B', False, True))