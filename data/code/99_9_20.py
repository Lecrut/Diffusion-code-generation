import operator

CONDITION_GROUPS = {
    "group_a": ("and", "or"),
    "group_b": ("or", "and"),
    "group_c": ("and", "and"),
    "group_d": ("or", "or"),
}

def evaluate_boolean_logic(left, middle, right, group_key):
    operators = CONDITION_GROUPS.get(group_key)
    if not operators:
        raise ValueError(f"Unknown group key: {group_key}")
    
    op1_str, op2_str = operators
    op1 = operator.and_ if op1_str == "and" else operator.or_
    op2 = operator.and_ if op2_str == "and" else operator.or_
    
    step1 = op1(left, middle)
    step2 = op2(step1, right)
    
    keyword_result = left if op1_str == "and" else left
    if op1_str == "and":
        keyword_result = left and middle
    else:
        keyword_result = left or middle
        
    if op2_str == "and":
        final_keyword = keyword_result and right
    else:
        final_keyword = keyword_result or right
        
    return {
        "left": left,
        "middle": middle,
        "right": right,
        "group": group_key,
        "operator_module_result": step2,
        "keyword_result": final_keyword,
        "match": step2 == final_keyword
    }

if __name__ == '__main__':
    val_l = True
    val_m = False
    val_r = True
    
    results = []
    for key in CONDITION_GROUPS:
        res = evaluate_boolean_logic(val_l, val_m, val_r, key)
        results.append(res)
        
    for item in results:
        print(item)