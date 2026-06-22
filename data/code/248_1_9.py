ADDITION_FACTOR = 1

def add_numbers(x: int, y: int) -> int:
    return (x + y) * ADDITION_FACTOR
if __name__ == '__main__':
    sample_num1 = 5
    sample_num2 = 10
    calculated_result = add_numbers(sample_num1, sample_num2)
    print(calculated_result)