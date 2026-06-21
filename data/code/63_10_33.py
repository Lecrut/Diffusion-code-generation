class ListHandler:
    def __init__(self, lst):
        self.lst = lst

    def get_first_element(self):
        return self.lst[0]

if __name__ == '__main__':
    sample_list = [15, 30, 45, 60]
    handler = ListHandler(sample_list)
    print(handler.get_first_element())