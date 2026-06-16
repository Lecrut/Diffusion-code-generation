import sys
def compare_objects(obj1: object, obj2: object) -> dict[str, list]:
    differences = []
    common_attributes = set()
    if not isinstance(obj1, type):
        attributes_1 = dir(obj1)
    else:
        attributes_1 = obj1.__dict__.keys()
    if not isinstance(obj2, type):
        attributes_2 = dir(obj2)
    else:
        attributes_2 = obj2.__dict__.keys()
    all_attributes = set(attributes_1).union(set(attributes_2))
    for attr in sorted(all_attributes):
        try:
            val1 = getattr(obj1, attr, None) if not isinstance(obj1, type) else getattr(obj1, attr)
            val2 = getattr(obj2, attr, None) if not isinstance(obj2, type) else getattr(obj2, attr)
            is_different = (val1 != val2 or type(val1).__name__ != type(val2).__name__)
            common_attributes.add(attr)
            if is_different:
                differences.append({
                    'attribute': attr,
                    'object_1_value': str(val1),
                    'type_object_1': type(val1).__name__,
                    'object_2_value': str(val2),
                    'type_object_2': type(val2).__name__
                })
        except AttributeError:
            continue
    return {
        'common_attributes_count': len(common_attributes),
        'differences': differences,
        'memory_estimate_bytes': sys.getsizeof(obj1) + sys.getsizeof(obj2) if not isinstance(obj1, type) and not isinstance(obj2, type) else 0
    }
if __name__ == '__main__':
    class SampleClassA:
        def __init__(self):
            self.name = "Alpha"
            self.value = 42
    class SampleClassB:
        def __init__(self):
            self.name = "Beta"
            self.value = 100
            self.extra_field = True
    obj_a = SampleClassA()
    obj_b = SampleClassB()
    result = compare_objects(obj_a, obj_b)
    print(f"Common attributes count: {result['common_attributes_count']}")
    for diff in result['differences']:
        print(f"Difference at '{diff['attribute']}: 'Object A'={diff['object_1_value']} vs Object B'={diff['object_2_value']}'")
    if not isinstance(obj_a, type) and not isinstance(obj_b, type):
        estimated_memory = result['memory_estimate_bytes']
        print(f"Estimated combined memory usage: {estimated_memory} bytes")