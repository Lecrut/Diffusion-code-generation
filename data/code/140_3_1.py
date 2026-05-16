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
            value_str = conditions.get('value')
            if value_str is not None:
                value = int(value_str)
                result = value
        except ValueError:
            result = "Error: Invalid value for calculation"
    else:
        result = "Condition not met or invalid operation"
    print(result)