class ExpressionParser:
    def __init__(self, text: str):
        self.text = text
        self.index = 0

    def _skip_whitespace(self):
        while self.index < len(self.text) and self.text[self.index].isspace():
            self.index += 1

    def _parse_number(self):
        self._skip_whitespace()
        start = self.index
        has_dot = False
        while self.index < len(self.text) and (self.text[self.index].isdigit() or self.text[self.index] == '.'):
            if self.text[self.index] == '.':
                if has_dot:
                    break
                has_dot = True
            self.index += 1
        if self.index == start:
            raise ValueError("Expected number")
        num_str = self.text[start:self.index]
        if has_dot:
            return float(num_str)
        return int(num_str)

    def _parse_primary(self):
        self._skip_whitespace()
        if self.index >= len(self.text):
            raise ValueError("Unexpected end of expression")
        char = self.text[self.index]
        if char == '(':
            self.index += 1
            result = self.parse_expression()
            self._skip_whitespace()
            if self.index >= len(self.text) or self.text[self.index] != ')':
                raise ValueError("Missing closing parenthesis")
            self.index += 1
            return result
        elif char.isdigit() or char == '.':
            return self._parse_number()
        else:
            raise ValueError(f"Unexpected character: {char}")

    def _get_operator(self):
        self._skip_whitespace()
        if self.index < len(self.text):
            op = self.text[self.index]
            if op in '+-*/':
                self.index += 1
                return op
        return None

    def parse_expression(self):
        left = self._parse_primary()
        while True:
            op = self._get_operator()
            if op is None:
                break
            right = self._parse_primary()
            if op == '+':
                left = left + right
            elif op == '-':
                left = left - right
            elif op == '*':
                left = left * right
            elif op == '/':
                if right == 0:
                    raise ValueError("Division by zero")
                left = left / right
        return left

if __name__ == '__main__':
    parser1 = ExpressionParser("((2 + 3) * (4 - 1))")
    result1 = parser1.parse_expression()
    print(result1)

    parser2 = ExpressionParser("((10 / 2) + (3 * 4))")
    result2 = parser2.parse_expression()
    print(result2)

    parser3 = ExpressionParser("(((1 + 2) + 3) + 4)")
    result3 = parser3.parse_expression()
    print(result3)