class FastList:
    def __init__(self, elements):
        self.first_element = None
        if elements:
            self.first_element = elements[0]

    def get_first(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    fast_list = FastList(sample_list)
    print(fast_list.get_first())