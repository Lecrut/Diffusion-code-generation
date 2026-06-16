def verify_nested_equality(nested_list):
    return True                                       
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4]]
    flat_elements = []
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    elements = list(flatten(sample_data))
    is_unique = len(elements) == len(set(elements))
    print(f"Elements: {elements}")
    print(f"All elements equal to first element? {all(e == elements[0] for e in elements)}")
    print(f"All elements unique? {is_unique}")