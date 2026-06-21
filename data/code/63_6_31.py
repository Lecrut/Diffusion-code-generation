class ListWrapper:
    def __init__(self, lst):
        self.lst = lst

    def first_element(self):
        if not self.lst:
            raise ValueError("List is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    wrapper = ListWrapper(sample_list)
    print(wrapper.first_element())