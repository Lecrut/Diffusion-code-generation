def check_equality(a: any, b: any) -> bool:
    if not isinstance(a, type(b)):
        raise ValueError("Types do not match")
    return a == b

if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality("hello", "hello"))
    try:
        print(check_equality(10, "10"))
    except ValueError as e:
        print(e)