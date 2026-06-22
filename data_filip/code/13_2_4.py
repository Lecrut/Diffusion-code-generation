def snake_to_camel(s: str) -> str:
    if not s:
        return ""
    
    parts = s.split('_')
    
    if parts[0] == '':
        if s.startswith('_'):
            parts[0] = '_'
        else:
            parts[0] = ''
    
    if len(parts) == 1:
        return parts[0]
    
    result_parts = [parts[0]]
    
    for part in parts[1:]:
        if part == '':
            continue
        result_parts.append(part.capitalize())
        
    return ''.join(result_parts)

if __name__ == '__main__':
    print(snake_to_camel("snake_case"))
    print(snake_to_camel("leading_underscore"))
    print(snake_to_camel("__double_underscore"))
    print(snake_to_camel("trailing_underscore_"))
    print(snake_to_camel("multiple___underscores"))
    print(snake_to_camel("alreadyCamel"))
    print(snake_to_camel("_start_and_end_"))
    print(snake_to_camel(""))
    print(snake_to_camel("a"))
    print(snake_to_camel("a_b_c_d_e"))