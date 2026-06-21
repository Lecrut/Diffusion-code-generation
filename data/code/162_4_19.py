from collections import namedtuple

NameValue = namedtuple('NameValue', ['name', 'value'])

def create_frozen_mapping(name_values):
    return tuple(name_value._asdict() for name_value in name_values)

if __name__ == '__main__':
    sample_name_values = [
        NameValue(name="apple", value=1),
        NameValue(name="banana", value=2),
        NameValue(name="cherry", value=3)
    ]
    frozen_mapping = create_frozen_mapping(sample_name_values)
    
    for entry in frozen_mapping:
        print(entry['name'], entry['value'])