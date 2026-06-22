is_negative = lambda x: x < 0

if __name__ == '__main__':
    test_values = [-20, 5, -1, 0, 30]
    for value in test_values:
        result = is_negative(value)
        print(f"is_negative({value}) = {result}")