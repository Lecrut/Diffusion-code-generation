def get_first_element(sequence):
    iterator = iter(sequence)
    return next(iterator)

if __name__ == '__main__':
    items = ['one', 'two', 'three']
    output = get_first_element(items)
    print(output)