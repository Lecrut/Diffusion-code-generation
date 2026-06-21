import threading

class ItemCounter:
    _instance = None
    _lock = threading.Lock()
    _item_counts = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ItemCounter, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def update_count(item, amount=1):
        with ItemCounter._lock:
            if item in ItemCounter._item_counts:
                ItemCounter._item_counts[item] += amount
            else:
                ItemCounter._item_counts[item] = amount

    @staticmethod
    def get_total_unique_items():
        with ItemCounter._lock:
            return len(ItemCounter._item_counts)

if __name__ == '__main__':
    counter = ItemCounter()
    counter.update_count('apple', 3)
    counter.update_count('banana')
    counter.update_count('apple', 2)
    print(counter.get_total_unique_items())