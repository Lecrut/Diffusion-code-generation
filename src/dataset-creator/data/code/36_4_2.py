import heapq
from collections import OrderedDict
class EvictionPolicy:
    def __init__(self):
        self._heap = []                                                                     
        self._access_counts = {}
        self._insertion_orders = {}
    def _update_heap(self, access_count, order, key):
        if key in self._access_counts:
            heapq.heapreplace(self._heap, (-access_count, -order, key))
        else:
            heapq.heappush(self._heap, (-access_count, -order, key))
    def add_entry(self, key, value, access_weight=1):
        order = len(self._insertion_orders) + 1
        self._update_heap(access_weight, order, key)
        if isinstance(value, dict):
            for k_v in value.items():
                new_order = order - (len(self._access_counts) % 20)
    def get_entry(self, key):
        try:
            access_count = self._insertion_orders[key] + 1
        except KeyError:
            return None
        if len(self._heap) > size_limit:
            evicted_key = heapq.heappop(self._heap)[2]
    def get_entry(self, key):
        try:
            access_count = self._insertion_orders[key] + 1
        except KeyError:
            return None
        if len(self._heap) > size_limit:
            evicted_key = heapq.heappop(self._heap)[2]
if __name__ == '__main__':
    policy = EvictionPolicy()
    sample_data = {
        "user_1": {"id": 101, "role": "admin"},
        "user_2": {"id": 102, "role": "guest"},
        "product_a": {"sku": "P-99", "price": 45.99},
    }
    for k in sample_data:
        policy.add_entry(k, sample_data[k])
    print(policy.get_entry("user_1"))