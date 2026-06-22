def fetch_second_element(elements):
    if len(elements) < 2:
        raise ValueError("The list must contain at least two elements.")
    return elements[1]

if __name__ == '__main__':
    sample_data = ["one", "two", "three", "four"]
    try:
        second_item = fetch_second_element(sample_data)
        print(second_item)
    except ValueError as ve:
        print(ve)