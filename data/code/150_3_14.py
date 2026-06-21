class ListModifier:
    @staticmethod
    def remove_integer(lst, target):
        try:
            index = lst.index(target)
            lst.pop(index)
        except ValueError:
            return

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    integer_to_remove = 30
    ListModifier.remove_integer(sample_list, integer_to_remove)
    print(sample_list)