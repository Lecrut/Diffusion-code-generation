def is_in_checklist(element, checklist):
    return element in checklist

if __name__ == '__main__':
    sample_element = 'apple'
    sample_checklist = frozenset(['apple', 'banana', 'cherry'])
    print(is_in_checklist(sample_element, sample_checklist))