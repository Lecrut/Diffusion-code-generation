def get_first_last(iterable):
    try:
        return iterable[0], iterable[-1]
    except IndexError:
        return None, None

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3, 4, 5],
        ['a', 'b'],
        [],
        [10]
    ]
    for value in sample_values:
        print(f"List: {value}, First and Last: {get_first_last(value)}")