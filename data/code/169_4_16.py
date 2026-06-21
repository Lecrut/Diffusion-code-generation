import threading

class ItemCounter:
    _instance = None
    _lock = threading.Lock()
    _item_counts = {}
    
    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ItemCounter, cls).__new__(cls)
        return cls._instance
    
    @staticmethod
    def update_count(item, amount=1):
        with ItemCounter._lock:
            if item in ItemCounter._item_counts:
                ItemCounter._item_counts[item] += amount
            else:
                ItemCounter._item_counts[item] = amount
    
    @classmethod
    def get_total_unique_items(cls):
        with cls._lock:
            return len(cls._item_counts)

if __name__ == '__main__':
    ic1 = ItemCounter()
    ic2 = ItemCounter()
    
    ic1.update_count('apple', 3)
    ic2.update_count('banana', 5)
    ic1.update_count('apple', 2)
    
    print(f"Total unique items: {ItemCounter.get_total_unique_items()}")