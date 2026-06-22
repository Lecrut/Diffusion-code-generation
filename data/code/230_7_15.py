def map_to_upper(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings.")
    return list(map(lambda x: x.upper(), strings))

if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "programming"]
    try:
        uppercased_list = map_to_upper(sample_list)
        print(uppercased_list)
    except ValueError as e:
        print(e)