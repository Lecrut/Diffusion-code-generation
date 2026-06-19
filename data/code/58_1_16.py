def get_first_element(data):
    try:
        return data[0]
    except IndexError as e:
        print("Error: The list is empty.")
        raise

if __name__ == '__main__':
    my_list = [15, 25, 35, 45]
    try:
        first = get_first_element(my_list)
        print(first)
    except Exception as e:
        print(e)