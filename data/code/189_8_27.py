def remove_elements(predicate, lst):
    return [x for x in lst if not predicate(x)]

class ElementFilter:
    def __init__(self, lst):
        self.lst = lst
    
    def filter_out(self, predicate):
        self.lst = remove_elements(predicate, self.lst)
    
    def get_filtered_list(self):
        return self.lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate = lambda x: x % 2 == 0
    filter_instance = ElementFilter(sample_list)
    filter_instance.filter_out(predicate)
    print(filter_instance.get_filtered_list())