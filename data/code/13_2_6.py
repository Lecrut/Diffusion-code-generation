def snake_to_camel(name):
    if not name:
        return ""
    
    parts = name.split("_")
    
    if parts[0] == "":
        leading_underscores = 1
        if len(parts) > 1 and parts[1] == "":
            leading_underscores = 2
            parts = parts[2:]
        else:
            parts = parts[1:]
    else:
        leading_underscores = 0
    
    if not parts:
        if leading_underscores:
            return "_" * leading_underscores
        return ""
    
    capitalized_parts = []
    for i, part in enumerate(parts):
        if not part:
            continue
        if i == 0:
            if leading_underscores:
                capitalized_parts.append(part.lower())
            else:
                capitalized_parts.append(part.lower())
        else:
            capitalized_parts.append(part.capitalize())
    
    result = "".join(capitalized_parts)
    
    if leading_underscores:
        result = "_" * leading_underscores + result
        
    return result

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("_private_method"))
    print(snake_to_camel("__dunder_var"))
    print(snake_to_camel("alreadyCamel"))
    print(snake_to_camel("multiple___underscores_here"))
    print(snake_to_camel("single"))
    print(snake_to_camel(""))
    print(snake_to_camel("_"))
    print(snake_to_camel("foo_bar_baz"))