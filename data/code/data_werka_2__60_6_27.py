class SafeListHandler:
    def __init__(self, lst):
        self.lst = lst

    def get_last_element(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[-1]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    handler_1 = SafeListHandler(sample_list_1)
    try:
        print(handler_1.get_last_element())
    except ValueError as e:
        print(e)

    empty_list = []
    handler_2 = SafeListHandler(empty_list)
    try:
        print(handler_2.get_last_element())
    except ValueError as e:
        print(e)

    sample_list_3 = [9, 8, 7, 6]
    handler_3 = SafeListHandler(sample_list_3)
    try:
        print(handler_3.get_last_element())
    except ValueError as e:
        print(e)