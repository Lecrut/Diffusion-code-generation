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
        print(f"Error occurred while comparing {type(a)} and {type(b)}. Reason: {e}")
        raise
if __name__ == '__main__':
    sample_int = 5
    another_int = 5
    same_obj = [1, 2, 3]
    print(check_equality(sample_int, another_int))       
    list_a = []
    list_b = []
    print(check_equality(list_a, list_b))                            
    string_a = "hello"
    string_b = "hello"
    same_string_obj = "world"
    print(check_equality(string_a, string_b))       
    try:
        check_equality(same_obj, [1, 2])
    except Exception as e:
        pass