def replace_spaces_with_underscores(s: str) -> str:
    return s.replace(' ', '_')
if __name__ == '__main__':
    sample_strings = ['hello world', 'multiple   spaces   here', 'no_spaces_here', ' leading and trailing ', 'mixed\ttabs and spaces', '', 'single']
    for sample in sample_strings:
        result = replace_spaces_with_underscores(sample)
        print(f'Input:  {repr(sample)}')
        print(f'Output: {repr(result)}')
        print('-' * 40)