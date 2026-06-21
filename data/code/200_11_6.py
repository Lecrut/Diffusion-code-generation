def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    for item in data:
        if not isinstance(item, int):
            raise ValueError("All elements in the list must be integers.")

def every_second_element(data):
    validate_input(data)
    for index in range(0, len(data), 2):
        yield data[index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gen = every_second_element(sample_list)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))