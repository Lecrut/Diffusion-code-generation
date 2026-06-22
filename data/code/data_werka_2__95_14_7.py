def check_conditions(first: float, second: float, third: float) -> bool:
    conditions = {
        'positive_first': first > 0,
        'second_less_than_first': second < first,
        'third_equals_sum': third == first + second
    }
    return all(conditions.values())

if __name__ == '__main__':
    result = check_conditions(10.0, 4.0, 14.0)
    print(result)