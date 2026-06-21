def element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, list):
                raise ValueError("The function must return a list.")
            try:
                return result[index]
            except IndexError:
                raise IndexError(f"Index {index} is out of range for the returned list.")
        return wrapper
    return decorator

class DataFetcher:
    def __init__(self, data_source):
        self.data_source = data_source

    @element_retriever(2)
    def fetch_element(self):
        return self.data_source

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    fetcher = DataFetcher(sample_data)
    print(fetcher.fetch_element())

    another_sample_data = ['alpha', 'beta', 'gamma', 'delta']
    another_fetcher = DataFetcher(another_sample_data)
    print(another_fetcher.fetch_element())