def check_equality(a: any, b: any) -> bool:
    if type(a) != type(b):
        return False
    try:
        a_id = id(a)
        b_id = id(b)
        if isinstance(a, (int, float)) and not isinstance(a, bool):
            return a == b
        elif isinstance(a, str):
            return a is b or a == b
        else:
            return a is b
    except Exception as e:
        print(f"Error occurred during comparison: {e}")
        return False
if __name__ == '__main__':
    sample_int = 5
    another_int = 5
    same_str = "hello"
    result1 = check_equality(sample_int, another_int)
    result2 = check_equality(same_str, same_str)