def evaluate_conditions(string_a: str, string_b: str, num_x: int, num_y: int) -> bool:
    return string_a == string_b and num_x != num_y

if __name__ == '__main__':
    result = evaluate_conditions("hello", "hello", 10, 20)
    print(result)