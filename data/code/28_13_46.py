def is_larger_than(first_number, second_number):
    return first_number > second_number

if __name__ == '__main__':
    comparison_values = [(10, 5), (20, 30), (15, 7)]
    for num1, num2 in comparison_values:
        result = is_larger_than(num1, num2)
        print(f"{num1} > {num2}: {result}")