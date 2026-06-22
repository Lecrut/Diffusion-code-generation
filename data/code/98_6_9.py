def evaluate_conditions(str_a: str, str_b: str, num_a: int, num_b: int) -> str:
    if str_a == str_b and num_a != num_b:
        return "Conditions met: strings equal and numbers unequal"
    return "Conditions not met"

if __name__ == '__main__':
    result = evaluate_conditions("hello", "hello", 10, 20)
    print(result)