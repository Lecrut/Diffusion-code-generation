if __name__ == '__main__':
    my_list = [False, False, True, False]
    if any(my_list):
        print("At least one element is True")
    else:
        print("All elements are False")