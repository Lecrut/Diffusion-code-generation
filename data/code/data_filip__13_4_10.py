import re

def snake_to_camel(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_inputs = ['hello_world', 'this_is_a_test_string', 'single', 'a_b_c_d']
    results = [snake_to_camel(s) for s in sample_inputs]
    for original, converted in zip(sample_inputs, results):
        print(f"{original} -> {converted}")