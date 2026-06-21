class ListModifier:
    def __init__(self, initial_list):
        self.data = initial_list

    def remove_integer(self, target):
        try:
            index = self.data.index(target)
            self.data.pop(index)
        except ValueError:
            return

if __name__ == '__main__':
    modifier = ListModifier([10, 20, 30, 40, 50])
    modifier.remove_integer(30)
    print(modifier.data)