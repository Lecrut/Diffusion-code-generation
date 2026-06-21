def remove_spaces(text):
    space_map = {ord(' '): None}
    return text.translate(str.maketrans(space_map))
if __name__ == '__main__':
    sample_text = 'This is another example with spaces.'
    result = remove_spaces(sample_text)
    print(result)