class FastElementRetriever:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
        self.first_element = elements[0] if elements else None

    def retrieve_first(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    retriever = FastElementRetriever(sample_list)
    print(retriever.retrieve_first())