class BooleanEvaluator:
    OPERATOR_PRECEDENCE = {
        'not': 3,
        'and': 2,
        'or': 1
    }

    @staticmethod
    def _apply_operator(op, left, right):
        if op == 'and':
            return left and right
        if op == 'or':
            return left or right
        if op == 'not':
            return not left
        raise ValueError(f'Unsupported operator: {op}')

    @staticmethod
    def _parse_expression(tokens):
        if not tokens:
            return False
        i = 0
        current_value = False
        if isinstance(tokens[i], bool):
            current_value = tokens[i]
            i += 1
        while i < len(tokens):
            op = tokens[i]
            if not isinstance(op, str):
                break
            if op not in BooleanEvaluator.OPERATOR_PRECEDENCE:
                break
            i += 1
            if i < len(tokens) and isinstance(tokens[i], bool):
                next_value = tokens[i]
                i += 1
                if op == 'and':
                    current_value = current_value and next_value
                elif op == 'or':
                    current_value = current_value or next_value
                elif op == 'not':
                    current_value = not next_value
                else:
                    raise ValueError(f'Unsupported operator: {op}')
            else:
                if op == 'not':
                    current_value = not current_value
                else:
                    raise ValueError('Missing operand for operator')
        return current_value

    @classmethod
    def evaluate(cls, conditions):
        if not conditions:
            return False
        tokens = []
        for item in conditions:
            if isinstance(item, bool):
                tokens.append(item)
            elif isinstance(item, str):
                lower_item = item.lower()
                if lower_item in cls.OPERATOR_PRECEDENCE:
                    tokens.append(lower_item)
                else:
                    raise ValueError(f'Unsupported condition: {item}')
            else:
                raise ValueError(f'Unsupported input type: {type(item)}')
        return cls._parse_expression(tokens)

if __name__ == '__main__':
    sample_conditions = [True, 'and', False, 'or', True, 'and', True]
    result = BooleanEvaluator.evaluate(sample_conditions)
    print(result)