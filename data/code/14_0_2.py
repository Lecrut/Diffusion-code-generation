def get_third_element(items):
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    try:
        result = get_third_element(sample_list)
        print(result)
    except IndexError as e:
        print(e)
    
    short_list = [1, 2]
    try:
        result = get_third_element(short_list)
        print(result)
    except IndexError as e:
        print(e)