def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    
    parts = snake_str.split('_')
    
    if not parts:
        return ""
    
    leading_underscores = 0
    idx = 0
    n = len(parts)
    while idx < n and parts[idx] == '':
        leading_underscores += 1
        idx += 1
    
    non_empty_parts = parts[idx:]
    
    if not non_empty_parts:
        return '_' * leading_underscores
    
    camel_parts = [non_empty_parts[0]]
    for part in non_empty_parts[1:]:
        if part:
            camel_parts.append(part.capitalize())
        else:
            camel_parts.append('_')
            
    result = ''.join(camel_parts)
    
    if leading_underscores > 0:
        result = '_' * leading_underscores + result
        
    return result

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("__private_method"))
    print(snake_to_camel("alreadyCamel"))
    print(snake_to_camel("multi_word_name_here"))
    print(snake_to_camel("_start_with_one"))
    print(snake_to_camel("double__underscore__test"))
    print(snake_to_camel(""))
    print(snake_to_camel("___leading_and_trailing__"))
    print(snake_to_camel("a"))
    print(snake_to_camel("_"))