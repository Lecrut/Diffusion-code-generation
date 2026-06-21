class ElementRetriever:
    def __init__(self, index):
        self.index = index

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, list):
                raise ValueError("The function must return a list.")
            try:
                return result[self.index]
            except IndexError:
                raise IndexError(f"Index {self.index} is out of range for the returned list.")
        return wrapper

@ElementRetriever(4)
def fetch_items():
    return ['one', 'two', 'three', 'four', 'five']

if __name__ == '__main__':
    print(fetch_items())