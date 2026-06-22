class SafeListRetriever:
    def __init__(self, data):
        self._data = data

    @classmethod
    def get_safe_element(cls, instance, index):
        if 0 <= index < len(instance._data):
            return instance._data[index]
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [15, 25, 35, 45, 55]
    retriever_instance = SafeListRetriever(SAMPLE_LIST)
    print(SafeListRetriever.get_safe_element(retriever_instance, 3))
    print(SafeListRetriever.get_safe_element(retriever_instance, -1))
    print(SafeListRetriever.get_safe_element(retriever_instance, 5))
    print(SafeListRetriever.get_safe_element(retriever_instance, 0))