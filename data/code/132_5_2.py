def logic_sequence():
    bool_dict = {1: True, 2: False}
    for key in sorted(bool_dict.keys()):
        yield bool_dict[key] and bool_dict[3 - key]

if __name__ == '__main__':
    print(list(logic_sequence()))