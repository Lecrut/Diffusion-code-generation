config_mapping = {
    (1, 'a'): 'value1',
    (2, 'b'): 'value2',
    (3, 'c'): 'value3'
}

if __name__ == '__main__':
    print(config_mapping[(1, 'a')])
    print(config_mapping[(2, 'b')])
    print(config_mapping[(3, 'c')])