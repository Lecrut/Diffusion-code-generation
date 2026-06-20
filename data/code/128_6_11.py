def is_negative(number: float) -> bool:
    return number < 0
if __name__ == '__main__':
    sample_values = [-10.5, 3.2, -0.001, 0, 10]
    for value in sample_values:
        result = is_negative(value)
        print(f'is_negative({value}) is {result}')