def concatenate_generator(list1, list2):
    yield from list1
    yield from list2

class ListConcatenator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    
    def get_concatenated(self):
        return concatenate_generator(self.list1, self.list2)

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenator = ListConcatenator(list1, list2)
    
    concatenated_gen = concatenator.get_concatenated()
    print("Concatenated elements:")
    for item in concatenated_gen:
        print(item)