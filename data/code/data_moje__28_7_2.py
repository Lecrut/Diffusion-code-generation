def sort_descending(num1: float, num2: float) -> tuple[float, float]:
    if num1 >= num2:
        return (num1, num2)
    return (num2, num1)

if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 5
    result = sort_descending(sample_num1, sample_num2)
    print(result)
    another_sample_num1 = 3.5
    another_sample_num2 = 7.2
    another_result = sort_descending(another_sample_num1, another_sample_num2)
    print(another_result)