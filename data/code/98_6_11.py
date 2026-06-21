def check_conditions(str_a: str, str_b: str, num_x: int, num_y: int) -> str:
    if str_a == str_b and num_x != num_y:
        return "Conditions met"
    return "Conditions not met"

if __name__ == '__main__':
    result = check_conditions("hello", "hello", 10, 20)
    print(result)