import heapq
from typing import Any, Dict, List
class EvictionPolicy:
    def __init__(self):
        pass
    @staticmethod
    def evict_by_size(items: List[tuple], max_items: int) -> None:
        if len(items) > max_items:
            items.pop(0)
class FrequencyBasedEviction(EvictionPolicy):
    def __init__(self, min_access_count: int = 1):
        self.min_access_count = min_access_count
    @staticmethod
    def evict_by_frequency(items: List[tuple], max_items: int) -> None:
        if len(items) > max_items:
            sorted_indices = sorted(range(len(items)), key=lambda i: items[i][1])
            evicted_idx = min(sorted_indices[:max(0, len(items)-max_items)])
            heapq.heappop(items)
class DynamicLookupTable:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.data: Dict[Any, Any] = {}
        self.access_history: List[tuple] = []                                                            
    def get(self, key: Any) -> Any:
        if key not in self.data:
            return None
        count = self.data[key].get('access_count', 0) + 1
        self.data[key]['access_count'] = count
        try:
            heapq.heappush(self.access_history, (-count, key))
        except IndexError:
            pass
        return self.data[key]
    def set(self, key: Any, value: Any) -> None:
        if len(self.data) >= self.max_size and not (key in self.data):
            while len(self.access_history) > 0 and -self.access_history[0][1] < self.min_access_count:
                heapq.heappop(self.access_history)
            if len(self.data) >= self.max_size:
                evicted_key = next(iter([k for k, v in self.data.items()]))
                del self.data[evicted_key]
        self.data[key] = {'value': value}
class ProductionLookupTable(DynamicLookupTable):
    def __init__(self, max_size: int = 100):
        super().__init__(max_size)
    def get(self, key: Any) -> Any:
        result = self.data.get(key)
        if result is not None and 'value' in result:
            return result['value']
        while len(self.access_history) > 0 and -self.access_history[0][1] < 2:
            heapq.heappop(self.access_history)
        if len(self.data) >= self.max_size:
            evicted_key = next(iter([k for k, v in self.data.items()]))
            del self.data[evicted_key]
        return None
    def set(self, key: Any, value: Any) -> bool:
        while len(self.access_history) > 0 and -self.access_history[0][1] < self.min_access_count:
            heapq.heappop(self.access_history)
        if len(self.data) >= self.max_size and key not in self.data:
            evicted_key = next(iter([k for k, v in self.data.items()]))
            del self.data[evicted_key]
        self.data[key] = {'value': value}
        return True
if __name__ == '__main__':
    table = ProductionLookupTable(max_size=5)
    sample_data = [
        ("apple", 10),
        ("banana", 20),
        ("cherry", 30),
        ("date", 40),
        ("elderberry", 50),
        ("fig", 60),
        ("grape", 70)
    ]
    for key, value in sample_data:
        table.set(key, value)
    print("Initial state:", list(table.data.keys()))
    table.get("apple")
    table.get("banana")
    table.get("cherry")
    for key in ["fig", "grape"]:
        table.set(key, 80)
    print("Final state:", list(table.data.keys()))