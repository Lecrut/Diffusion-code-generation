def get_first_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_list = [42, 73, 101]
    try:
        first_element = get_first_element(sample_list)
        print(f"The first element of {sample_list} is {first_element}")
    except ValueError as e:
        print(e)