class OperatorPrecedence:
    def __init__(self):
        self.ops = {
            'or': 1,
            'xor': 2,
            'and': 3,
            'shift': 4,
            'add': 5,
            'mul': 6,
            'pow': 7
        }
        self.sym_to_name = {
            '|': 'or', '^': 'xor', '&': 'and',
            '<<': 'shift', '>>': 'shift',
            '+': 'add', '-': 'add',
            '*': 'mul', '/': 'mul', '//': 'mul', '%': 'mul',
            '**': 'pow'
        }
        self.name_to_sym = {v: k for k, v in self.sym_to_name.items()}
        self.name_to_sym['pow'] = '**'

    def tokenize(self, expr):
        tokens = []
        i = 0
        length = len(expr)
        while i < length:
            char = expr[i]
            if char.isspace():
                i += 1
                continue
            if char in self.sym_to_name:
                key = char
                if i + 1 < length and expr[i:i+2] in self.sym_to_name:
                    key = expr[i:i+2]
                tokens.append(('op', self.sym_to_name[key], key))
                i += 2 if key in ('<<', '>>', '**') else 1
                continue
            if char.isdigit() or (char == '-' and i + 1 < length and expr[i+1].isdigit()):
                j = i
                if char == '-':
                    j += 1
                while j < length and expr[j].isdigit():
                    j += 1
                tokens.append(('num', int(expr[i:j]), expr[i:j]))
                i = j
                continue
            raise ValueError(f"Unexpected character: {char}")
        return tokens

    def parse(self, expr):
        tokens = self.tokenize(expr)
        if not tokens:
            return []
        result = []
        self._parse_expr(tokens, 0, len(tokens), result, 0)
        return result

    def _parse_expr(self, tokens, start, end, result, min_prec):
        if start >= end:
            return
        i = start
        current_op = None
        current_sym = None
        while i < end:
            if tokens[i][0] == 'num':
                i += 1
                continue
            if tokens[i][0] == 'op':
                op_name = tokens[i][1]
                prec = self.ops[op_name]
                if prec < min_prec:
                    break
                if current_op is None or prec > self.ops[current_op]:
                    current_op = op_name
                    current_sym = tokens[i][2]
                i += 1
            else:
                i += 1
        if current_op is None:
            for j in range(start, end):
                if tokens[j][0] == 'num':
                    result.append(tokens[j][2])
            return
        split_idx = start
        for j in range(start, end):
            if tokens[j][0] == 'op' and tokens[j][1] == current_op:
                split_idx = j
                break
        self._parse_expr(tokens, start, split_idx, result, self.ops[current_op] + 1)
        result.append(current_sym)
        self._parse_expr(tokens, split_idx + 1, end, result, self.ops[current_op] + 1)

    def get_precedence(self, symbol):
        return self.ops[self.sym_to_name[symbol]]

if __name__ == '__main__':
    parser = OperatorPrecedence()
    expr = "2 + 3 * 4"
    print(f"Parsed: {parser.parse(expr)}")
    print(f"Precedence of *: {parser.get_precedence('*')}")
    print(f"Precedence of +: {parser.get_precedence('+')}")
    print(f"Precedence of **: {parser.get_precedence('**')}")
    print(f"Precedence of //: {parser.get_precedence('//')}")
    print(f"Precedence of %: {parser.get_precedence('%')}")
    print(f"Precedence of /: {parser.get_precedence('/')}")
    print(f"Precedence of *: {parser.get_precedence('*')}")