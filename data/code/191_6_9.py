def combine_lists(list_alpha, list_beta):
    if not isinstance(list_alpha, list) or not isinstance(list_beta, list):
        raise ValueError("Both arguments must be lists.")
    return list_alpha + list_beta

if __name__ == '__main__':
    try:
        list_a = ["apple", "banana"]
        list_b = ["cherry", "date"]
        combined = combine_lists(list_a, list_b)
        print(combined)
    except ValueError as e:
        print(e)