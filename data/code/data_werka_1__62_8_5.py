def validate_collection(collection):
    if not isinstance(collection, list):
        raise TypeError("The provided collection must be a list.")
    if len(collection) < 2:
        raise ValueError("The provided collection does not have at least two elements.")

def get_second_item(lst):
    validate_collection(lst)
    return lst[1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        second_item = get_second_item(sample_list)
        print(second_item)
    except (TypeError, ValueError) as e:
        print(e)