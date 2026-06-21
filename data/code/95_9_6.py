def combine_checks(is_positive, is_even, is_less_than_100):
    conditions = []
    if is_positive:
        conditions.append("positive")
    if is_even:
        conditions.append("even")
    if is_less_than_100:
        conditions.append("less than 100")
    
    if not conditions:
        return "no conditions met"
    
    return " and ".join(conditions)

if __name__ == '__main__':
    result = combine_checks(True, True, True)
    print(result)