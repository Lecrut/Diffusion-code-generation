def evaluate_conditions(str_a: str, str_b: str, num_x: int, num_y: int) -> bool:
    return str_a == str_b and num_x != num_y

if __name__ == '__main__':
    result = evaluate_conditions("hello", "hello", 10, 20)
    print(result)