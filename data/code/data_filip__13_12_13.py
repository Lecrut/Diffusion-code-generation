def snake_to_camel(s):
    result = []
    upper_next = False
    for i, char in enumerate(s):
        if char == '_':
            upper_next = True
        else:
            if upper_next:
                result.append(char.upper())
                upper_next = False
            else:
                if i == 0:
                    result.append(char.lower())
                else:
                    result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    print(snake_to_camel("my_variable_name"))