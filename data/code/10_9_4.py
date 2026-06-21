def get_first_element(items):
    if not items:
        raise ValueError("List cannot be empty")
    return items[0]

if __name__ == '__main__':
    sample_list = [42, 100, 55]
    print(get_first_element(sample_list))
    empty_list = []
    try:
        get_first_element(empty_list)
    except ValueError as e:
        print(f"Error: {e}")