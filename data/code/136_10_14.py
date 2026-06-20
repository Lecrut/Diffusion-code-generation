def logical_operators_demo():
    values = {
        'a': True,
        'b': False,
        'c': True
    }
    
    and_result = values['a'] and values['b']
    or_result = values['a'] or values['b']
    not_a_result = not values['a']
    
    print("--- Logical Operators Demonstration ---")
    print(f"a = {values['a']}, b = {values['b']}, c = {values['c']}")
    print("\n--- Results ---")
    print(f"a AND b: {and_result}")
    print(f"a OR b: {or_result}")
    print(f"NOT a: {not_a_result}")

if __name__ == '__main__':
    logical_operators_demo()