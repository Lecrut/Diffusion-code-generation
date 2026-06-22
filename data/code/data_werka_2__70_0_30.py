def check_first_and_last(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    return lst[0], lst[-1]

class ListHandler:
    def __init__(self, lst):
        self.lst = lst

    def get_first_and_last(self):
        return check_first_and_last(self.lst)

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    handler = ListHandler(sample_list)
    first, last = handler.get_first_and_last()
    print(first, last)