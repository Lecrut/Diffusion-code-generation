def check_conditions(conditions):
    return any(condition() for condition in conditions)

if __name__ == '__main__':
    def is_even(n):
        return n % 2 == 0

    def is_divisible_by_three(n):
        return n % 3 == 0

    sample_values = [5, 10, 15, 20]
    conditions = [is_even, is_divisible_by_three]

    for value in sample_values:
        if check_conditions(conditions):
            print(f"At least one condition met for {value}")
        else:
            print(f"No conditions met for {value}")