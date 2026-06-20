class IterableProcessor:
    @staticmethod
    def get_first_last(iterable):
        try:
            return iterable[0], iterable[-1]
        except IndexError:
            return None, None

if __name__ == '__main__':
    processor = IterableProcessor()
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b']
    list3 = []
    
    print(f"List 1: {processor.get_first_last(list1)}")
    print(f"List 2: {processor.get_first_last(list2)}")
    print(f"List 3: {processor.get_first_last(list3)}")