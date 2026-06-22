def validate_combination(first: int, second: int, third: int) -> bool:
    positive_check = first > 0
    even_check = second % 2 == 0
    product = first * second
    if not positive_check or not even_check or product == 0:
        return False
    divisibility_check = third % product == 0
    return divisibility_check

if __name__ == '__main__':
    num_a = 5
    num_b = 2
    num_c = 10
    outcome = validate_combination(num_a, num_b, num_c)
    print(outcome)