def trim_spaces(text):
    return text.strip()

if __name__ == '__main__':
    sample = '  hello world  '
    print(trim_spaces(sample))
    sample_empty = '   '
    print(trim_spaces(sample_empty))
    sample_none = None
    try:
        print(trim_spaces(sample_none))
    except AttributeError:
        print('AttributeError handled')
    sample_normal = 'no_spaces'
    print(trim_spaces(sample_normal))