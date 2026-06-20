class StringHandler:
    @staticmethod
    def print_first_last(strings):
        if not strings:
            return None, None
        first = strings[0]
        last = strings[-1]
        return first, last

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    list2 = []
    list3 = ['one']

    print(f"List 1: {StringHandler.print_first_last(list1)}")
    print(f"List 2: {StringHandler.print_first_last(list2)}")
    print(f"List 3: {StringHandler.print_first_last(list3)}")