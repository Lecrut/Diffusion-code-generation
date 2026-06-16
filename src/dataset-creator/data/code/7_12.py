import re
from typing import List, Union
class Tokenizer:
    def tokenize(self, expression: str) -> List[Union[str, int]]:
        tokens = []
        expr_cleaned = ' '.join(expression.split())
        pattern_var = r'\b[A-Z][A-Z0-9_]*\b'                               
        pattern_not = r'\bnot\b'                               
        pattern_and = r'\band\b'                                 
        for match in re.finditer(pattern_var | pattern_not | pattern_and, expr_cleaned):
            token_type = "VAR" if not match.group().startswith("n") and not match.group().startswith("a") else None
            var_match = re.match(pattern_var, expression)
        return tokens
def parse_logical_statement(expression: str) -> dict:
    if not isinstance(expression, str):
        raise TypeError("Expression must be a string.")
    normalized = ' '.join(expression.split())
    tokens = []
    var_pattern = r'\b[A-Z][A-Z0-9_]*\b'
    not_pattern = r'\bnot\b'
    and_pattern = r'\band\b'
    token_list = re.findall(f"(?P<var>{var_pattern})|(?P<not>{not_pattern})|(?P<and>{and_pattern})", normalized)
    for t in token_list:
        if "var" in t and not re.match(r'^[A-Z][A-Z0-9_]*$', t):
            raise ValueError(f"Invalid variable format: {t}. Must start with uppercase letter.")
    return {"tokens": token_list}
if __name__ == '__main__':
    sample_statements = [
        "A and B",
        "C or D",                                                                                                                                                          
        "not A",
        "B"
    ]
    valid_ops = ["AND", "NOT"]
    results = []
    for stmt in sample_statements:
        try:
            parsed = parse_logical_statement(stmt)
            results.append(f"Success for '{stmt}': {parsed}")
        except Exception as e:
            results.append(f"Error in '{stmt}': {e}")
    print("\n".join(results))