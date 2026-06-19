def get_second_item(lst):
    def validate_list_length():
        if len(lst) < 2:
            raise IndexError("List must contain at least two elements.")
    
    validate_list_length()
    return lst[1]

if __name__ == '__main__':
    sample_list = [4, 14, 24]
    try:
        print(get_second_item(sample_list))
    except IndexError as e:
        print(e)