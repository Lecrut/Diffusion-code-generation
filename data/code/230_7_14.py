def to_upper(strings):
    return list(map(lambda s: s.upper(), strings))

if __name__ == '__main__':
    sample_values = ['hello', 'world', 'python', 'programming']
    uppercased_values = to_upper(sample_values)
    print(uppercased_values)