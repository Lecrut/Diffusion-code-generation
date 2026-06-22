import re
from typing import List, Tuple, Any

class BooleanEvaluator:
    def check_precedence(self, expression_string: str) -> List[Tuple[str, str, int]]:
        expression_string = expression_string.strip()
        if not expression_string:
            raise ValueError("Empty expression")

        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("No tokens found")

        precedence_map = {
            '(': 0,
            ')': 0,
            'or': 1,
            'and': 2,
            'not': 3,
        }

        operators = ['or', 'and', 'not']
        precedence_results = []

        stack = []
        output_queue = []

        for token in tokens:
            if token in operators:
                while (stack and stack[-1] != '(' and
                       precedence_map.get(stack[-1], 0) >= precedence_map[token]):
                    op = stack.pop()
                    output_queue.append(op)
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    op = stack.pop()
                    output_queue.append(op)
                if stack and stack[-1] == '(':
                    stack.pop()
            else:
                output_queue.append(token)

        while stack:
            op = stack.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(op)

        evaluation_order = []
        eval_stack = []
        current_precedence_level = 0

        for token in output_queue:
            if token in operators:
                current_precedence_level += 1
                eval_stack.append(token)
                evaluation_order.append((token, f"Level {current_precedence_level}", current_precedence_level))
            else:
                if eval_stack:
                    op = eval_stack.pop()
                    evaluation_order.append((op, f"Level {current_precedence_level}", current_precedence_level))

        return evaluation_order

    def _tokenize(self, expression: str) -> List[str]:
        pattern = r'\(|\)|\bnot\b|\band\b|\bor\b|\bTrue\b|\bFalse\b|\btrue\b|\bfalse\b|\bTRUE\b|\bFALSE\b|\s+'
        parts = re.split(pattern, expression)
        tokens = []
        for part in parts:
            if not part:
                continue
            lower_part = part.lower()
            if lower_part == 'true':
                tokens.append('True')
            elif lower_part == 'false':
                tokens.append('False')
            elif lower_part in ('and', 'or', 'not'):
                tokens.append(lower_part)
            elif part in ('(', ')'):
                tokens.append(part)
            else:
                raise ValueError(f"Unknown token: {part}")
        return tokens

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr = "True and False or not True"
    result = evaluator.check_precedence(expr)
    print(result)