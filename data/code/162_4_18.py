from collections import namedtuple

NameValue = namedtuple('NameValue', ['name', 'value'])

def create_frozen_mapping(name_values):
    return tuple(NameValue(name, value) for name, value in name_values)

if __name__ == '__main__':
    sample_name_values = [('apple', 1), ('banana', 2), ('cherry', 3)]
    frozen_mapping = create_frozen_mapping(sample_name_values)
    print(frozen_mapping)