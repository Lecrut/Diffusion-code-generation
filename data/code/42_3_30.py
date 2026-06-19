def build_spaced_string(input_list):
    if not input_list:
        return ''
    return ' '.join(map(str, input_list))
if __name__ == '__main__':
    sample_values = {'fruits': ['apple', 'banana', 'cherry', 'date'], 'numbers': [10, 20, 30, 40], 'mixed': [True, None, 3.14, 'hello']}
    for key, value in sample_values.items():
        output = build_spaced_string(value)
        print(f'{key.capitalize()}: {output}')