if __name__ == '__main__':
    input_data = "condition:true,value:10,operation:add"
    parts = input_data.split(',')
    conditions = {}
    for part in parts:
        key_value = part.split(':')
        if len(key_value) == 2:
            key = key_value[0].strip()
            value = key_value[1].strip()
            conditions[key] = value
    result = None
    if conditions.get('condition') == 'true' and conditions.get('operation') == 'add':
        try:
            a = int(conditions.get('value', 0))
            b = 5                                              
            result = a + b
        except ValueError:
            result = "Error: Invalid numeric value"
    else:
        result = "Condition not met or operation mismatch"
    print(result)