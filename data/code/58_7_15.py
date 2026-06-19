def get_first_element(data):
    if not data:
        raise ValueError('The input list is empty.')
    return data[0]
if __name__ == '__main__':
    try:
        sample1 = [5, 10, 15]
        sample2 = ['x', 'y', 'z']
        sample3 = []
        sample4 = [999]
        print(f'First element of {sample1}: {get_first_element(sample1)}')
        print(f'First element of {sample2}: {get_first_element(sample2)}')
        print(f'First element of {sample4}: {get_first_element(sample4)}')
        print(f'First element of {sample3}: {get_first_element(sample3)}')
    except ValueError as e:
        print(e)