def evaluate_conditions(x: int, y: int, z: bool) -> str:
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, bool):
        raise ValueError("Invalid input types. x and y must be integers, and z must be a boolean.")
    
    if x > 10 and y < 5:
        return "Condition 1 met"
    elif z:
        return "Condition 2 met"
    else:
        return "No specific condition met"

if __name__ == '__main__':
    try:
        var_x = 15
        var_y = 3
        var_z = False
        output = evaluate_conditions(var_x, var_y, var_z)
        print(output)
        
        var_x = 5
        var_y = 8
        var_z = True
        output = evaluate_conditions(var_x, var_y, var_z)
        print(output)
    except ValueError as e:
        print(e)