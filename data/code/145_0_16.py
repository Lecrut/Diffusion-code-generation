def check_nested_conditions(a: bool, b: bool, c: bool) -> bool:
    intermediate_result = a and (not b) or (c and b)
    return intermediate_result
if __name__ == '__main__':
    a = True
    b = False
    c = True
    result = check_nested_conditions(a, b, c)
    print(result)