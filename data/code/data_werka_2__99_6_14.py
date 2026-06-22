import re
from typing import List, Tuple, Union

class BooleanExpressionAnalyzer:
    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = [
            ["NOT"],
            ["AND"],
            ["OR"]
        ]
        self.parsed_tree = self._parse()
        self.result = self._evaluate(self.parsed_tree)

    def _tokenize(self, expression: str) -> List[str]:
        cleaned = expression.replace(" ", "")
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'\b(AND|OR|NOT|TRUE|FALSE)\b|[\(\)]'
        matches = re.findall(pattern, cleaned)
        if len(matches) == 0:
            raise ValueError("No valid tokens found")
        if len(matches) != len(re.findall(pattern, cleaned)):
            raise ValueError("Invalid characters in expression")
        return matches

    def _parse(self) -> dict:
        pos = [0]
        result = self._parse_or()
        if pos[0] != len(self.tokens):
            raise ValueError("Unexpected token at end of expression")
        return result

    def _parse_or(self) -> dict:
        left = self._parse_and()
        while pos[0] < len(self.tokens) and self.tokens[pos[0]] == "OR":
            pos[0] += 1
            right = self._parse_and()
            left = {"op": "OR", "left": left, "right": right}
        return left

    def _parse_and(self) -> dict:
        left = self._parse_not()
        while pos[0] < len(self.tokens) and self.tokens[pos[0]] == "AND":
            pos[0] += 1
            right = self._parse_not()
            left = {"op": "AND", "left": left, "right": right}
        return left

    def _parse_not(self) -> dict:
        if pos[0] < len(self.tokens) and self.tokens[pos[0]] == "NOT":
            pos[0] += 1
            operand = self._parse_not()
            return {"op": "NOT", "operand": operand}
        return self._parse_primary()

    def _parse_primary(self) -> dict:
        if pos[0] >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        token = self.tokens[pos[0]]
        if token == "(":
            pos[0] += 1
            expr = self._parse_or()
            if pos[0] >= len(self.tokens) or self.tokens[pos[0]] != ")":
                raise ValueError("Missing closing parenthesis")
            pos[0] += 1
            return expr
        if token in ("TRUE", "FALSE"):
            pos[0] += 1
            return {"val": token == "TRUE"}
        raise ValueError(f"Unexpected token: {token}")

    def _evaluate(self, node: dict) -> bool:
        if "val" in node:
            return node["val"]
        op = node["op"]
        if op == "NOT":
            return not self._evaluate(node["operand"])
        if op == "AND":
            return self._evaluate(node["left"]) and self._evaluate(node["right"])
        if op == "OR":
            return self._evaluate(node["left"]) or self._evaluate(node["right"])
        raise ValueError(f"Unknown operator: {op}")

    def get_result(self) -> bool:
        return self.result

    def get_precedence_documentation(self) -> List[List[str]]:
        return self.precedence_rules

if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer("TRUE AND NOT FALSE OR FALSE")
    print(analyzer.get_result())
    print(analyzer.get_precedence_documentation())