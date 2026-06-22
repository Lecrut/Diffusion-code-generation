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
def retrieve_elements():
    return [100, 200, 300, 400, 500, 600]

if __name__ == '__main__':
    print(retrieve_elements())