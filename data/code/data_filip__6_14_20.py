def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')
if __name__ == '__main__':
    sample_inputs = ['Hello World', 'Python   programming', 'No spaces here', '  Leading and trailing  ', '', '   ', 'One space', 'Multiple    spaces    here', 'Tab\tand\tspace', 'Newline\nand space']
    for sample in sample_inputs:
        result = replace_spaces_with_underscores(sample)
        print(f'Input: {repr(sample)} -> Output: {repr(result)}')