if __name__ == '__main__':
    input_data = "condition:true,value:10,operation:add"
    parts = input_data.split(',')
    conditions = {}
    for part in parts:
        key, value = part.split(':', 1)
        conditions[key.strip()] = value.strip()
    result = None
    if conditions.get('condition') == 'true' and conditions.get('operation') == 'add':
        try:
            operand1 = int(conditions.get('value', 0))
            operand2 = 5                                              
            result = operand1 + operand2
        except ValueError:
            result = "Error: Invalid number format"
    else:
        result = "Condition not met or invalid operation"
    print(result)