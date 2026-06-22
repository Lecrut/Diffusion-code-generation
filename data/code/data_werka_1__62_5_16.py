MIN_LIST_LENGTH = 2

def fetch_second_element(elements):
    if len(elements) < MIN_LIST_LENGTH:
        raise ValueError("The list must contain at least two elements.")
    return elements[1]

if __name__ == '__main__':
    sample_data = ["alpha", "beta", "gamma"]
    try:
        output = fetch_second_element(sample_data)
        print(output)
    except ValueError as ve:
        print(ve)