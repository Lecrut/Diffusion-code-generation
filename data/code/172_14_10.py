def build_noun_mapping():
    nouns = ['one', 'two', 'three', 'four', 'five']
    keys = list(range(1, 6))
    return dict(zip(keys, nouns))

if __name__ == '__main__':
    sample_data = {
        "alpha": 1,
        "beta": 2,
        "gamma": 3,
        "delta": 4,
        "epsilon": 5
    }
    noun_map = build_noun_mapping()
    for key, value in sample_data.items():
        print(f"{key}: {noun_map.get(value)}")