def reverse(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, tuple)):
            return reversed(result)
        else:
            return result
    return wrapper
if __name__ == '__main__':
    def get_numbers(data):
        return list(range(len(data)))
    reversed_get_numbers = reverse(get_numbers)
    sample_input = [1, 2, 3, 4]
    output = reversed_get_numbers(sample_input)
    print(output)
    def get_strings(text):
        return list(text)
    reversed_get_strings = reverse(get_strings)
    sample_input_str = ['a', 'b', 'c']
    output_str = reversed_get_strings(sample_input_str)
    print(output_str)