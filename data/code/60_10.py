def get_last_item(data):
    if not data:
        raise IndexError("Cannot get the last item from an empty list")
    return data[-1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    empty_list = []
    try:
        result1 = get_last_item(list1)
        print(f"The last item of {list1} is: {result1}")
        result2 = get_last_item(list2)
        print(f"The last item of {list2} is: {result2}")
        try:
            get_last_item(empty_list)
        except IndexError as e:
            print(f"Error for empty list: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")