from collections import defaultdict

class ItemCounter:
    HASHABLE_TYPES = (int, str, float, bool)
    
    @staticmethod
    def convert_non_hashable(item):
        if isinstance(item, list):
            return tuple(item)
        raise TypeError("Non-hashable type encountered")
    
    def count_items(self, data_list):
        counter = defaultdict(int)
        for item in data_list:
            try:
                if not isinstance(item, self.HASHABLE_TYPES):
                    item = self.convert_non_hashable(item)
                counter[item] += 1
            except TypeError as e:
                print(f"Error processing {item}: {e}")
        return dict(counter)

if __name__ == '__main__':
    ic = ItemCounter()
    list1 = [1, "a", 3.14, True]
    list2 = []
    list3 = ["hello", None, []]
    list4 = [5]
    
    print(f"Count for list1: {ic.count_items(list1)}")
    print(f"Count for list2: {ic.count_items(list2)}")
    print(f"Count for list3: {ic.count_items(list3)}")
    print(f"Count for list4: {ic.count_items(list4)}")