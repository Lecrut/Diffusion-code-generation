TRUE = True
FALSE = False

def logical_operators_demo():
    a = TRUE
    b = FALSE
    print('--- Logical Operators Demonstration ---')
    print(f'a = {a}, b = {b}')
    and_result = a and b
    or_result = a or b
    not_a_result = not a
    print('\n--- Results ---')
    print(f'a AND b: {and_result}')
    print(f'a OR b: {or_result}')
    print(f'NOT a: {not_a_result}')
if __name__ == '__main__':
    logical_operators_demo()