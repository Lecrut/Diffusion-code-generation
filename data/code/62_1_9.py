def validate_list_length(lst):
    if len(lst) < 2:
        raise IndexError("List does not have a second item.")

def get_second_item(lst):
    validate_list_length(lst)
    return lst[1]

if __name__ == '__main__':
    sample_list = [9, 19, 29]
    try:
        print(get_second_item(sample_list))
    except IndexError as e:
        print(e)