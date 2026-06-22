def get_second_item(lst):
    return lst[1] if len(lst) > 1 else None

class ItemRetriever:
    def __init__(self, items):
        self.items = items
    def retrieve_second(self):
        return get_second_item(self.items)

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = [5]
    retriever_1 = ItemRetriever(sample_list_1)
    retriever_2 = ItemRetriever(sample_list_2)
    print(retriever_1.retrieve_second())
    print(retriever_2.retrieve_second())