def map_integers_to_strings(int_dict):
    return {k: str(v) for k, v in int_dict.items()}

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 5: 6}
    mapped_dict = map_integers_to_strings(sample_dict)
    print(mapped_dict)