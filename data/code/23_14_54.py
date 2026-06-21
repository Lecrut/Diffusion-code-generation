def compare_values(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both arguments must be numbers')
        return (a > b) - (a < b)
    except Exception as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    result1 = compare_values(7, 3)
    print(result1)
    result2 = compare_values(4, 4)
    print(result2)
    result3 = compare_values(9, 15)
    print(result3)
    result4 = compare_values('a', 15)
    print(result4)