class SafeListRetriever:
    def __init__(self, items):
        self._items = items
    
    @classmethod
    def get_safe(cls, instance, idx):
        if 0 <= idx < len(instance._items):
            return instance._items[idx]
        return None

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    retriever = SafeListRetriever(example_list)
    print(SafeListRetriever.get_safe(retriever, 3))
    print(SafeListRetriever.get_safe(retriever, -1))
    print(SafeListRetriever.get_safe(retriever, 5))