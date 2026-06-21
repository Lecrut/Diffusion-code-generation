class ElementRetriever:
    def __init__(self, collection):
        self.collection = collection

    def retrieve_first(self):
        if not self.collection:
            raise ValueError("The collection is empty and has no first element.")
        return self.collection[0]

if __name__ == '__main__':
    sample_list = [12, 24, 36, 48]
    retriever = ElementRetriever(sample_list)
    try:
        first_element = retriever.retrieve_first()
        print(first_element)
    except ValueError as e:
        print(f"Error: {e}")

    empty_list = []
    empty_retriever = ElementRetriever(empty_list)
    try:
        first_element = empty_retriever.retrieve_first()
        print(first_element)
    except ValueError as e:
        print(f"Error: {e}")