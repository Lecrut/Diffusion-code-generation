class ElementFilter:
    def __init__(self, lst):
        self.lst = lst

    def remove_elements(self, predicate):
        return [x for x in self.lst if not predicate(x)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate = lambda x: x % 2 == 0
    filter_instance = ElementFilter(sample_list)
    result = filter_instance.remove_elements(predicate)
    print(result)