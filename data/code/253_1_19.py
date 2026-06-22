def find_the_middle_value_among_three_validate(a, b, c):
    try:
        values = [float(x) for x in (a, b, c)]
        if len(values) != 3:
            raise ValueError('Exactly three numeric values are required.')
        return sorted(values)[1]
    except ValueError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    result = find_the_middle_value_among_three_validate(5, 10, 7)
    print(result)