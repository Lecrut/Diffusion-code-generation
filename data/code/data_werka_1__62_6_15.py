class SafeListWrapper:
    def __init__(self, elements):
        self.elements = elements

    def safe_second(self):
        try:
            return self.elements[1]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    wrapper = SafeListWrapper(sample_list)
    print(wrapper.safe_second())

    empty_list = []
    empty_wrapper = SafeListWrapper(empty_list)
    print(empty_wrapper.safe_second())