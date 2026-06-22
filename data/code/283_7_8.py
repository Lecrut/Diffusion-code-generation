def all_elements_equal(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    return len(set(lst)) == 1

if __name__ == '__main__':
    sample_list = [42, 42, 42]
    try:
        output = all_elements_equal(sample_list)
        print(output)
    except ValueError as e:
        print(e)