def evaluate_conditions(str_a: str, str_b: str, num_x: float, num_y: float) -> str:
    if str_a == str_b and num_x != num_y:
        return "Conditions Met"
    return "Conditions Not Met"

if __name__ == '__main__':
    result = evaluate_conditions("test", "test", 10, 20)
    print(result)