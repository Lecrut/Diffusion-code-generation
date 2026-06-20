def starts_with_a_or_b(strings):
    for s in strings:
        if s.startswith('A') or s.startswith('B'):
            return True
    return False

if __name__ == '__main__':
    sample_list1 = ['Apple', 'Banana', 'Cherry']
    sample_list2 = ['Orange', 'Grape', 'Melon']
    print(f"List 1 starts with A or B: {starts_with_a_or_b(sample_list1)}")
    print(f"List 2 starts with A or B: {starts_with_a_or_b(sample_list2)}")