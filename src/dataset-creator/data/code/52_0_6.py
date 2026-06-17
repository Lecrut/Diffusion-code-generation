def get_last_value(data):
    if not data:
        return None
    return data[-1]
if __name__ == '__main__':
    test_cases = [
        [10, 20, 30],
        ['a', 'b', 'c'],
        [],
        (5,),
        {'key': 'value'}
    ]
    for i, data in enumerate(test_cases):
        try:
            result = get_last_value(data)
            print(f"Input {i}: {data} -> Last value: {result}")
        except Exception as e:
            print(f"Input {i}: Error - {e}")