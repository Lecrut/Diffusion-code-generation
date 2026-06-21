class SubstringFinder:
    @staticmethod
    def create_set(data):
        return set(data)

    @staticmethod
    def item_exists(data, item):
        data_set = SubstringFinder.create_set(data)
        return item in data_set

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    item1 = 'banana'
    result1 = SubstringFinder.item_exists(list1, item1)
    print(f"List: {list1}, Item: {item1}, Exists: {result1}")

    list2 = ['dog', 'cat', 'bird']
    item2 = 'fish'
    result2 = SubstringFinder.item_exists(list2, item2)
    print(f"List: {list2}, Item: {item2}, Exists: {result2}")