def check_identity(a: any, b: any) -> bool:
    return a is b
if __name__ == '__main__':
    var1 = [1, 2, 3]
    var2 = [1, 2, 3]
    result_var = check_identity(var1, var2)
    int_a = 42
    int_b = 42
    result_int = check_identity(int_a, int_b)
    str_c = "hello"
    str_d = "hello"
    result_str = check_identity(str_c, str_d)
    print(f"List identity: {result_var}")
    print(f"Int identity: {result_int}")
    print(f"Str identity: {result_str}")