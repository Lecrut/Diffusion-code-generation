def group_by_length(strings):
    return {len(s): [s for s in strings if len(s) == l] for l in set(len(s) for s in strings)}

if __name__ == '__main__':
    sample_strings = ["hello", "world", "hi", "hey", "hola"]
    grouped_by_length = group_by_length(sample_strings)
    print(grouped_by_length)