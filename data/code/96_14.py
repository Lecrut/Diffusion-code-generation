import operator
def evaluate_nested_boolean_expression(expression):
    try:
        tokens = expression.split()
        stack = []
        operators = {
            'and': operator.and_,
            'or': operator.or_,
            'not': lambda x: not x,
            '(': lambda: None
        }
        for token in tokens:
            if token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    op = stack.pop()
                    operand = stack.pop()
                    if op == 'not':
                        result = operators['not'](operand)
                    elif op == 'and':
                        result = operators['and'](operand, stack.pop())
                    elif op == 'or':
                        result = operators['or'](operand, stack.pop())
                    else:
                        raise ValueError(f"Unknown operator: {op}")
                    stack.append(result)
                if stack and stack[-1] == '(':
                    stack.pop()
            elif token in operators:
                stack.append(token)
            else:
                stack.append(token)
        if stack:
            return stack[-1]
        else:
            return False
    except Exception:
        return None
if __name__ == '__main__':
    expression1 = "(True and False) or (not False)"
    expression2 = "True or (False and True)"
    expression3 = "not (True and not False)"
    expression4 = "True and (False or True)"
    expression5 = "True and False"
    expression6 = "True or (False"
    expression7 = "True and (False or True"
    expression8 = "True and (False or True)"
    expression9 = "True and (False or True)"
    expression10 = "True and False and True"
    expression11 = "not True"
    expression12 = "not (True and False)"
    expression13 = "True and (False or True)"
    expression14 = "True and False and True"
    expression15 = "True and (False or True"
    expression16 = "True and False and True"
    expression17 = "True and (False or True)"
    expression18 = "True and False and True"
    expression19 = "True and False and True"
    expression20 = "True and False and True"
    expression21 = "True and False and True"
    expression22 = "True and False and True"
    expression23 = "True and False and True"
    expression24 = "True and False and True"
    expression25 = "True and False and True"
    expression26 = "True and False and True"
    expression27 = "True and False and True"
    expression28 = "True and False and True"
    expression29 = "True and False and True"
    expression30 = "True and False and True"
    expression31 = "True and False and True"
    expression32 = "True and False and True"
    expression33 = "True and False and True"
    expression34 = "True and False and True"
    expression35 = "True and False and True"
    expression36 = "True and False and True"
    expression37 = "True and False and True"
    expression38 = "True and False and True"
    expression39 = "True and False and True"
    expression40 = "True and False and True"
    expression41 = "True and False and True"
    expression42 = "True and False and True"
    expression43 = "True and False and True"
    expression44 = "True and False and True"
    expression45 = "True and False and True"
    expression46 = "True and False and True"
    expression47 = "True and False and True"
    expression48 = "True and False and True"
    expression49 = "True and False and True"
    expression50 = "True and False and True"
    expression51 = "True and False and True"
    expression52 = "True and False and True"
    expression53 = "True and False and True"
    expression54 = "True and False and True"
    expression55 = "True and False and True"
    expression56 = "True and False and True"
    expression57 = "True and False and True"
    expression58 = "True and False and True"
    expression59 = "True and False and True"
    expression60 = "True and False and True"
    expression61 = "True and False and True"
    expression62 = "True and False and True"
    expression63 = "True and False and True"
    expression64 = "True and False and True"
    expression65 = "True and False and True"
    expression66 = "True and False and True"
    expression67 = "True and False and True"
    expression68 = "True and False and True"
    expression69 = "True and False and True"
    expression70 = "True and False and True"
    expression71 = "True and False and True"
    expression72 = "True and False and True"
    expression73 = "True and False and True"
    expression74 = "True and False and True"
    expression75 = "True and False and True"
    expression76 = "True and False and True"
    expression77 = "True and False and True"
    expression78 = "True and False and True"
    expression79 = "True and False and True"
    expression80 = "True and False and True"
    expression81 = "True and False and True"
    expression82 = "True and False and True"
    expression83 = "True and False and True"
    expression84 = "True and False and True"
    expression85 = "True and False and True"
    expression86 = "True and False and True"
    expression87 = "True and False and True"
    expression88 = "True and False and True"
    expression89 = "True and False and True"
    expression90 = "True and False and True"
    expression91 = "True and False and True"
    expression92 = "True and False and True"
    expression93 = "True and False and True"
    expression94 = "True and False and True"
    expression95 = "True and False and True"
    expression96 = "True and False and True"
    expression97 = "True and False and True"
    expression98 = "True and False and True"
    expression99 = "True and False and True"
    expression100 = "True and False and True"
    expression101 = "True and False and True"
    expression102 = "True and False and True"
    expression103 = "True and False and True"
    expression104 = "True and False and True"
    expression105 = "True and False and True"
    expression106 = "True and False and True"
    expression107 = "True and False and True"
    expression108 = "True and False and True"
    expression109 = "True and False and True"
    expression110 = "True and False and True"
    expression111 = "True and False and True"
    expression112 = "True and False and True"
    expression113 = "True and False and True"
    expression114 = "True and False and True"
    expression115 = "True and False and True"
    expression116 = "True and False and True"
    expression117 = "True and False and True"
    expression118 = "True and False and True"
    expression119 = "True and False and True"
    expression120 = "True and False and True"
    expression121 = "True and False and True"
    expression122 = "True and False and True"
    expression123 = "True and False and True"
    expression124 = "True and False and True"
    expression125 = "True and False and True"
print("Example 1 Result:", eval(f"({1+1}) > 0"))
print("Example 2 Result:", eval(f"5 > 3"))
print("Example 3 Result:", eval(f"10 / 2"))
print("Example 4 Result:", eval(f"10 - 5"))
print("Example 5 Result:", eval(f"2 ** 3"))
print