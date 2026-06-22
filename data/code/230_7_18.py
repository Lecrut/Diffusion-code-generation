UPPERCASE_MAP = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def map_to_uppercase(strings):
    return list(map(lambda s: s.translate(UPPERCASE_MAP), strings))

if __name__ == '__main__':
    sample_values = ['hello', 'world', 'python', 'programming']
    print(map_to_uppercase(sample_values))