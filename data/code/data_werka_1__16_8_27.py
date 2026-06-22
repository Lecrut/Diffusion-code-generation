def is_positive(number):
    return number > 0
if __name__ == '__main__':
    try:
        test_values = [10, -5, 0, 'a', None]
        results = []
        for value in test_values:
            if isinstance(value, int):
                result = is_positive(value)
                results.append(result)
            else:
                results.append(False)
        print(results)
    except Exception as e:
        print(e)