from collections import defaultdict
from functools import partial

class CompositeKeyStore:
    def __init__(self, default_factory):
        self.store = defaultdict(partial(self._nested_default, default_factory))
    
    def _nested_default(self, factory, key):
        return defaultdict(lambda: defaultdict(factory))

    def get_or_init(self, key1, key2, key3):
        if key1 not in self.store:
            self.store[key1] = self._nested_default(self.store.default_factory.default_factory.default_factory, key1)
        
        inner = self.store[key1]
        
        if key2 not in inner:
            inner[key2] = self._nested_default(self.store.default_factory.default_factory.default_factory, key2)
        
        inner2 = inner[key2]
        
        if key3 not in inner2:
            inner2[key3] = self.store.default_factory.default_factory.default_factory()
        
        return inner2[key3]

def create_number():
    return 42

def create_string():
    return "default_value"

def create_list():
    return []

if __name__ == '__main__':
    store = CompositeKeyStore(create_list)
    result_a = store.get_or_init("category", "subcategory", "item")
    result_b = store.get_or_init("category", "subcategory", "item")
    result_c = store.get_or_init("new_cat", "new_sub", "new_item")
    print(result_a)
    print(result_b)
    print(result_c)