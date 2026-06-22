def strip_whitespace_from_list(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_list = [
        '  hello  ',
        'world',
        '  python  programming  ',
        '  data   science',
        'machine learning  ',
        '  artificial  intelligence  ',
        'deep  learning  ',
        '  natural language processing  ',
        'computer vision  ',
        '  robotics  '
    ]
    result = strip_whitespace_from_list(sample_list)
    print(result)