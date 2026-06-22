def process_strings(tuple_strings):
    result = []
    for s in tuple_strings:
        result.append(s.capitalize())
    return tuple(result)

if __name__ == '__main__':
    sample_tuple = ('hello', 'WORLD', 'PyThOn', 'tEST', 'MiXeD')
    processed_tuple = process_strings(sample_tuple)
    print(processed_tuple)