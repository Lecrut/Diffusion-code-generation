class ItemChecker:
    @staticmethod
    def contains_item(lst, value):
        return value in set(lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'orange']
    print(ItemChecker.contains_item(sample_list, 'apple'))
    print(ItemChecker.contains_item(sample_list, 'grape'))