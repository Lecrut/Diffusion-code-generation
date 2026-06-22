def to_camel_case(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_inputs = ['snake_case_example', 'another_one_here', 'singleword', '']
    results = [to_camel_case(s) for s in sample_inputs]
    for original, converted in zip(sample_inputs, results):
        print(f'{original} -> {converted}')