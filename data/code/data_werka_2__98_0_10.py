def evaluate_flags(status_code, priority, is_valid):
    category_map = {
        200: "Success",
        404: "Not Found",
        500: "Server Error",
        403: "Forbidden",
        401: "Unauthorized"
    }
    priority_map = {
        1: "Critical",
        2: "High",
        3: "Medium",
        4: "Low"
    }
    
    if status_code not in category_map:
        raise ValueError(f"Unsupported status code: {status_code}")
    
    if priority not in priority_map:
        raise ValueError(f"Unsupported priority level: {priority}")

    if not is_valid:
        result = "Invalid Input"
    elif status_code == 200 and priority == 1:
        result = f"Critical Success: {category_map[status_code]}"
    elif status_code == 404:
        result = f"Missing Resource: {category_map[status_code]}"
    elif status_code == 500:
        result = f"System Failure: {category_map[status_code]}"
    else:
        result = f"Standard Event: {category_map[status_code]} at {priority_map[priority]} Priority"
    
    return result

if __name__ == '__main__':
    code = 200
    level = 1
    valid = True
    result = evaluate_flags(code, level, valid)
    print(result)
    
    code = 404
    level = 3
    valid = True
    result = evaluate_flags(code, level, valid)
    print(result)
    
    code = 500
    level = 2
    valid = False
    result = evaluate_flags(code, level, valid)
    print(result)