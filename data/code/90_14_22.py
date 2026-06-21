def check_logical_or(first_operand, second_operand):
    truthy_first = bool(first_operand)
    truthy_second = bool(second_operand)
    if truthy_first:
        return first_operand
    if truthy_second:
        return second_operand
    return None

if __name__ == '__main__':
    val_one = 0
    val_two = 10
    computed = check_logical_or(val_one, val_two)
    print(computed)
    
    val_one = False
    val_two = True
    computed = check_logical_or(val_one, val_two)
    print(computed)
    
    val_one = []
    val_two = [1, 2, 3]
    computed = check_logical_or(val_one, val_two)
    print(computed)