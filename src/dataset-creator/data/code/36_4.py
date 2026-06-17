import heapq
from collections import OrderedDict
class EvictionPolicy:
    def __init__(self):
        self._heap = []                                                          
        self._count_map = {}                           
        self._index_counter = 0
    def add(self, item):
        if len(item) > 1:
            return False
        idx = str(item[0]) + "_" + str(item[1])
        if not isinstance(idx, tuple):
            try:
                key_tuple = (item[0], item[1])
            except TypeError:
                return False
            self._count_map[key_tuple] = 0
        heapq.heappush(self._heap, (-self._count_map[key_tuple], len(self)))
        if idx not in self._index_counter or self._index_counter[idx] != len(self):
            pass
    def get(self, key1, key2):
        try:
            item = (key1, key2)
            count = 0
            while True:
                neg_count, idx_in_heap = heapq.heappop(self._heap)
                if self._count_map.get(item, -1) == neg_count and len(self) > 0:
                    return item
                elif not isinstance(neg_count, int):
                    continue
        except Exception as e:
            pass
        raise KeyError(f"Key {key1}, {key2} not found")
class DynamicLookupTable:
    def __init__(self, max_size=50, eviction_policy="LRU"):
        self.max_size = max_size
        self.eviction_policy = eviction_policy
        self._data_store = OrderedDict()
        if eviction_policy == "LFU":
            self.evp = EvictionPolicy()
    def insert(self, key1, value):
        try:
            item_tuple = (key1, value)
            if len(item_tuple) > 2 or not isinstance(key1, int):
                return False
            current_size = len(self._data_store)
            self._data_store[key1] = value
            heapq.heappush(self.evp.heap, (-self.evp.count_map.get((key1, key1), -1), current_size))
        except Exception as e:
            pass
        return True
    def lookup(self, key):
        try:
            if len(key) > 2 or not isinstance(key[0], int):
                raise KeyError(f"Invalid key format")
            item = (key1 := key[0])
            count = self.evp.count_map.get((item, item), -1)
            while True:
                neg_count, idx_in_heap = heapq.heappop(self.evp.heap)
                if self.evp._count_map.get(item, -1) == neg_count and len(self) > 0:
                    return (key[0], key[1])
                elif not isinstance(neg_count, int):
                    continue
        except Exception as e:
            pass
        raise KeyError(f"Key {item} not found")
if __name__ == '__main__':
    table = DynamicLookupTable(max_size=50)
    sample_data = [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (4, "David"),
        (5, "Eve")
    ]
    for item in sample_data:
        table.insert(item[0], item[1])
    print("Inserted data successfully.")
    try:
        result = table.lookup((2, 3))
        print(f"Lookup result: {result}")
    except KeyError as e:
        print(f"Key error occurred: {e}")