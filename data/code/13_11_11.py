def snake_to_camel(name):
    if not name:
        return name
    
    parts = name.split('_')
    if not parts:
        return name
    
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part.capitalize()
    return result

if __name__ == '__main__':
    sample = 'my_variable_name'
    result = snake_to_camel(sample)
    print(result)