from typing import Final

TRUE_CONST: Final = True
FALSE_CONST: Final = False

def flip_bool_value(value: bool) -> bool:
    if value is TRUE_CONST:
        result = FALSE_CONST
    else:
        result = TRUE_CONST
    return result

if __name__ == '__main__':
    input_val = True
    output_val = flip_bool_value(input_val)
    print(output_val)
    
    input_val_2 = False
    output_val_2 = flip_bool_value(input_val_2)
    print(output_val_2)