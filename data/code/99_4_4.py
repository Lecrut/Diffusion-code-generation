class ExpressionParser:
    def __init__(self, expression: str):
        self.expression = expression
        self.pos = 0

    def parse(self):
        if not self.expression:
            raise ValueError("Empty expression")
        self.expression = self.expression.strip()
        if not self.expression:
            raise ValueError("Empty expression")
        result = self._parse_expression()
        if self.pos < len(self.expression):
            raise ValueError(f"Unexpected character at index {self.pos}")
        return result

    def _parse_expression(self):
        left = self._parse_term()
        while self.pos < len(self.expression) and self.expression[self.pos] in ('+', '-'):
            op = self.expression[self.pos]
            self.pos += 1
            right = self._parse_term()
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left

    def _parse_term(self):
        left = self._parse_factor()
        while self.pos < len(self.expression) and self.expression[self.pos] in ('*', '/'):
            op = self.expression[self.pos]
            self.pos += 1
            right = self._parse_factor()
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                left = left / right
        return left

    def _parse_factor(self):
        if self.pos < len(self.expression) and self.expression[self.pos] == '(':
            self.pos += 1
            result = self._parse_expression()
            if self.pos >= len(self.expression) or self.expression[self.pos] != ')':
                raise ValueError("Missing closing parenthesis")
            self.pos += 1
            return result
        elif self.pos < len(self.expression) and self.expression[self.pos] in ('+', '-'):
            op = self.expression[self.pos]
            self.pos += 1
            val = self._parse_factor()
            if op == '-':
                return -val
            return val
        else:
            num_str = ""
            while self.pos < len(self.expression) and (self.expression[self.pos].isdigit() or self.expression[self.pos] == '.'):
                num_str += self.expression[self.pos]
                self.pos += 1
            if not num_str:
                raise ValueError("Expected number or parenthesis")
            if '.' in num_str:
                return float(num_str)
            else:
                return int(num_str)

if __name__ == '__main__':
    parser1 = ExpressionParser("(1+(2*3))")
    print(parser1.parse())

    parser2 = ExpressionParser("((10/2)+(3*4))")
    print(parser2.parse())

    parser3 = ExpressionParser("-((1+2))")
    print(parser3.parse())