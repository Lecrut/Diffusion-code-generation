def evaluate_condition(condition_string):
    if not condition_string:
        return False
    parts = condition_string.lower().split()
    if len(parts) == 0:
        return False
    conditions = []
    for part in parts:
        if part in ('and', 'or'):
            conditions.append(part)
        else:
            conditions.append(part)
    if not conditions:
        return False
    result = None
    current_state = None
    for i, part in enumerate(conditions):
        if part in ('and', 'or'):
            if i == 0:
                continue
            if len(conditions) <= i:
                return False
            if len(conditions) > i + 1:
                try:
                    operand1 = eval(conditions[i-1])
                    operand2 = eval(conditions[i+1])
                    if part == 'and':
                        current_state = operand1 and operand2
                    elif part == 'or':
                        current_state = operand1 or operand2
                except NameError:
                    return False
                except Exception:
                    return False
            else:
                return False
        else:
            try:
                value = eval(part)
                if current_state is None:
                    current_state = value
                else:
                    if part == 'and':
                        current_state = current_state and value
                    elif part == 'or':
                        current_state = current_state or value
            except NameError:
                return False
            except Exception:
                return False
    if current_state is not None:
        return current_state
    return False
if __name__ == '__main__':
    print(evaluate_condition("A and B"))
    print(evaluate_condition("True or False"))
    print(evaluate_condition("A and B and C"))
    print(evaluate_condition("False or True and False"))
    print(evaluate_condition("A and B and C and D"))
    print(evaluate_condition("A and B and X"))
    print(evaluate_condition("A and B"))
    print(evaluate_condition("A and B and C and D and E"))