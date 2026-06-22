from collections import namedtuple
from operator import eq

def run_length_encode(sequence):
    encoded = []
    iterator = iter(sequence)
    try:
        current_value = next(iterator)
    except StopIteration:
        return encoded
    
    count = 1
    
    for next_value in iterator:
        if next_value is current_value:
            count += 1
        elif next_value == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = next_value
            count = 1
    
    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4]
    result = run_length_encode(sample_sequence)
    print(result)
    
    class CustomObject:
        def __init__(self, value):
            self.value = value
        def __eq__(self, other):
            return isinstance(other, CustomObject) and self.value == other.value
        def __hash__(self):
            return hash(self.value)

    obj_a = CustomObject(10)
    sample_objects = [obj_a, obj_a, obj_a, CustomObject(20), CustomObject(20)]
    object_result = run_length_encode(sample_objects)
    print(object_result)