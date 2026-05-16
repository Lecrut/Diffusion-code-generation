def simulate_boolean_logic(vars, or_statements):
    results = {}
    for statement in or_statements:
        parts = statement.split(' ')
        if len(parts) == 3:
            var1, op, var2 = parts
            if op == 'or':
                if var1 in vars and var2 in vars:
                    results[f"{var1} or {var2}"] = vars[var1] or vars[var2]
                else:
                    results[f"{var1} or {var2}"] = None
    return results
if __name__ == '__main__':
    variables = {
        "A": True,
        "B": False,
        "C": True,
        "D": False
    }
    logic_statements = [
        "A or B",
        "B or C",
        "A or C",
        "D or A"
    ]
    simulation_results = simulate_boolean_logic(variables, logic_statements)
    print("Variables:", variables)
    print("Logic Statements:", logic_statements)
    print("Simulation Results:")
    for statement, result in simulation_results.items():
        print(f"{statement}: {result}")