def get_third_element(iterable):
    for i, item in enumerate(iterable):
        if i == 2:
            return item
    raise IndexError("Iterable does not have a third element")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        result = get_third_element(sample_data)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")